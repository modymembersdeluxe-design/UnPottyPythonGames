"""UnPotty Deluxe - comedic prototype generated from prompt ideas.

Controls:
- 1 / 2: choose options in each menu screen
- SPACE: perform the next mega action
- R: restart when finished
- ESC: quit
"""

from __future__ import annotations

import random
from enum import Enum, auto

import pygame

from asset_factory import prepare_all_assets
from game_data import CHARACTERS, COMPLETION_MESSAGES, LEVELS, MEGA_SCRIPT, TARGET_ITEMS


class Stage(Enum):
    CHARACTER_SELECT = auto()
    CLOTHES_SELECT = auto()
    LEVEL_SELECT = auto()
    PLAYING = auto()
    COMPLETE = auto()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1180, 720))
        pygame.display.set_caption("UnPotty Deluxe: Mega Collection")
        self.clock = pygame.time.Clock()
        self.big_font = pygame.font.SysFont("arial", 42, bold=True)
        self.font = pygame.font.SysFont("arial", 28)
        self.small = pygame.font.SysFont("arial", 22)

        self.assets = prepare_all_assets()
        self.stage = Stage.CHARACTER_SELECT
        self.selected_character = "Toddler"
        self.selected_clothes = "Remove pants"
        self.selected_level = LEVELS[0]

        self.script_index = 0
        self.defecate_count = 0
        self.fart_count = 0
        self.pee_count = 0
        self.current_target = random.choice(TARGET_ITEMS)
        self.log: list[str] = ["Let's go! Ready to go poo poo."]

        self._load_sounds()

    def _load_sounds(self) -> None:
        self.sfx = {}
        try:
            pygame.mixer.init()
            self.sfx["fart"] = pygame.mixer.Sound(str(self.assets["fart"]))
            self.sfx["poo"] = pygame.mixer.Sound(str(self.assets["poo"]))
            self.sfx["win"] = pygame.mixer.Sound(str(self.assets["win"]))
        except pygame.error:
            self.sfx = {}

    def play_sound(self, key: str) -> None:
        snd = self.sfx.get(key)
        if snd:
            snd.play()

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    self.handle_key(event.key)

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_key(self, key: int) -> None:
        if self.stage == Stage.CHARACTER_SELECT:
            if key == pygame.K_1:
                self.selected_character = "Toddler"
                self.stage = Stage.CLOTHES_SELECT
            elif key == pygame.K_2:
                self.selected_character = "Kid"
                self.stage = Stage.CLOTHES_SELECT

        elif self.stage == Stage.CLOTHES_SELECT:
            options = CHARACTERS[self.selected_character]["clothing"]
            if key == pygame.K_1:
                self.selected_clothes = options[0]
                self.stage = Stage.LEVEL_SELECT
            elif key == pygame.K_2 and len(options) > 1:
                self.selected_clothes = options[1]
                self.stage = Stage.LEVEL_SELECT

        elif self.stage == Stage.LEVEL_SELECT:
            if key in (pygame.K_1, pygame.K_2):
                self.selected_level = LEVELS[0]
                self.stage = Stage.PLAYING

        elif self.stage == Stage.PLAYING and key == pygame.K_SPACE:
            self.advance_sequence()

        elif self.stage == Stage.COMPLETE and key == pygame.K_r:
            self.__init__()

    def advance_sequence(self) -> None:
        script_line = MEGA_SCRIPT[self.script_index % len(MEGA_SCRIPT)]
        self.log.append(script_line)

        if "Defecate repeat 5" in script_line:
            self.defecate_count += 5
            self.fart_count += 5
            self.pee_count += 5
            self.play_sound("poo")
            self.play_sound("fart")
        elif "Fart longer" in script_line:
            self.fart_count += 5
            self.defecate_count += 1
            self.play_sound("fart")
        elif "Well done" in script_line:
            self.play_sound("win")

        self.current_target = random.choice(TARGET_ITEMS)
        self.script_index += 1

        if self.script_index >= len(MEGA_SCRIPT):
            self.log.extend(COMPLETION_MESSAGES)
            self.stage = Stage.COMPLETE

    def draw(self) -> None:
        self.screen.fill((26, 22, 35))
        self.draw_header()

        if self.stage == Stage.CHARACTER_SELECT:
            self.draw_character_select()
        elif self.stage == Stage.CLOTHES_SELECT:
            self.draw_clothes_select()
        elif self.stage == Stage.LEVEL_SELECT:
            self.draw_level_select()
        elif self.stage == Stage.PLAYING:
            self.draw_playing()
        elif self.stage == Stage.COMPLETE:
            self.draw_complete()

    def draw_header(self) -> None:
        title = self.big_font.render("UNPOTTY DELUXE SUPER MEGA COLLECTION", True, (255, 238, 120))
        self.screen.blit(title, (40, 18))

    def draw_character_select(self) -> None:
        t = self.font.render("Select Character: [1] Toddler  [2] Kid", True, (230, 230, 240))
        self.screen.blit(t, (60, 108))
        t2 = self.small.render("Feature: hands to hole + funny mega tummy feeling events.", True, (180, 210, 255))
        self.screen.blit(t2, (60, 148))

    def draw_clothes_select(self) -> None:
        options = CHARACTERS[self.selected_character]["clothing"]
        txt = self.font.render(f"{self.selected_character} selected. Choose clothes action:", True, (230, 230, 240))
        self.screen.blit(txt, (60, 112))
        op1 = self.small.render(f"[1] {options[0]}", True, (255, 255, 255))
        op2 = self.small.render(f"[2] {options[1]}", True, (255, 255, 255))
        self.screen.blit(op1, (80, 155))
        self.screen.blit(op2, (80, 186))

    def draw_level_select(self) -> None:
        txt = self.font.render("Level Select", True, (230, 230, 240))
        self.screen.blit(txt, (60, 110))
        lvl = self.small.render("[1] Mega Level Un-Potty  (Press 1 to start)", True, (255, 255, 255))
        self.screen.blit(lvl, (80, 154))

    def draw_playing(self) -> None:
        card = pygame.Rect(40, 100, 1090, 560)
        pygame.draw.rect(self.screen, (44, 36, 60), card, border_radius=20)

        stat = self.small.render(
            f"Character: {self.selected_character} | Clothes: {self.selected_clothes} | Level: {self.selected_level}",
            True,
            (225, 225, 225),
        )
        self.screen.blit(stat, (65, 122))
        target = self.small.render(f"Current target item: {self.current_target}", True, (255, 180, 180))
        self.screen.blit(target, (65, 154))

        counters = self.small.render(
            f"Defecate: {self.defecate_count}   Fart: {self.fart_count}   Pee: {self.pee_count}",
            True,
            (170, 255, 170),
        )
        self.screen.blit(counters, (65, 188))

        instr = self.small.render("Press SPACE to continue mega sequence", True, (190, 210, 250))
        self.screen.blit(instr, (65, 220))

        log_title = self.small.render("Action Log:", True, (255, 255, 255))
        self.screen.blit(log_title, (65, 264))
        recent = self.log[-10:]
        for i, line in enumerate(recent):
            line_surface = self.small.render(f"- {line}", True, (240, 240, 240))
            self.screen.blit(line_surface, (82, 294 + i * 28))

    def draw_complete(self) -> None:
        done = self.big_font.render("UN-POTTY COMPLETED", True, (140, 255, 140))
        self.screen.blit(done, (250, 180))

        lines = [
            "Well done! Great job! No clean up! Ewwwww smell!",
            "(laughing) more games unlocked.",
            "Press R to restart.",
        ]
        for i, line in enumerate(lines):
            surf = self.font.render(line, True, (230, 230, 240))
            self.screen.blit(surf, (170, 280 + i * 46))


def main() -> None:
    Game().run()


if __name__ == "__main__":
    main()
