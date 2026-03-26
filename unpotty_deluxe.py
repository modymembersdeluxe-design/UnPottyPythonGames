"""UnPotty Deluxe - comedic prototype generated from prompt ideas.

Controls:
- 1 / 2: choose options in each menu screen
- SPACE: perform the next mega action
- F/T/S/A/G/P/D/H/R/Y: trigger feature feeling sounds during gameplay
- M: cycle music tracks
- R: restart when finished
- ESC: quit
"""

from __future__ import annotations

from enum import Enum, auto

import pygame

from asset_factory import prepare_all_assets
from sprite_factory import render_character_pose, render_item_icon
from game_data import (
    BACKGROUND_COLORS,
    CHARACTERS,
    COMPLETION_MESSAGES,
    LEVELS,
    MANUAL_SOUND_KEYS,
    MEGA_STEPS,
    TARGET_ITEMS,
)


class Stage(Enum):
    CHARACTER_SELECT = auto()
    CLOTHES_SELECT = auto()
    LEVEL_SELECT = auto()
    PLAYING = auto()
    COMPLETE = auto()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 760))
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
        self.current_emotion = "neutral"
        self.shirt_on = True
        self.pants_on = True
        self.diaper_on = True

        self.script_index = 0
        self.target_index = 0
        self.defecate_count = 0
        self.fart_count = 0
        self.pee_count = 0
        self.current_target = TARGET_ITEMS[self.target_index]
        self.log: list[str] = ["Let's go! Ready to go poo poo."]
        self.frame_index = 0
        self.music_order = ["unpotty_trained", "unpotty_trainined", "poo_poo_song", "potty_failed"]
        self.music_idx = 0

        self._load_sounds()
        self._load_music()

    def _load_sounds(self) -> None:
        self.sfx: dict[str, pygame.mixer.Sound] = {}
        self.emotion_sfx: dict[str, pygame.mixer.Sound] = {}
        self.item_sfx: dict[str, pygame.mixer.Sound] = {}
        try:
            pygame.mixer.init()
            for key, path in self.assets["sounds"].items():
                self.sfx[key] = pygame.mixer.Sound(str(path))
            for key, path in self.assets["emotion_layers"].items():
                self.emotion_sfx[key] = pygame.mixer.Sound(str(path))
            for key, path in self.assets["item_sounds"].items():
                self.item_sfx[key] = pygame.mixer.Sound(str(path))
        except pygame.error:
            self.sfx = {}
            self.emotion_sfx = {}
            self.item_sfx = {}

    def _load_music(self) -> None:
        self.music_enabled = False
        try:
            start_path = self.assets["music"][self.music_order[self.music_idx]]
            pygame.mixer.music.load(str(start_path))
            pygame.mixer.music.play(-1)
            self.music_enabled = True
        except pygame.error:
            self.music_enabled = False

    def play_sound(self, key: str) -> None:
        snd = self.sfx.get(key)
        if snd:
            snd.play()

    def play_emotion_layer(self) -> None:
        snd = self.emotion_sfx.get(self.current_emotion)
        if snd:
            snd.play()

    def play_item_sound(self) -> None:
        snd = self.item_sfx.get(self.current_target)
        if snd:
            snd.play()

    def cycle_music(self) -> None:
        if not self.music_enabled:
            return
        self.music_idx = (self.music_idx + 1) % len(self.music_order)
        name = self.music_order[self.music_idx]
        path = self.assets["music"][name]
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play(-1)
        self.log.append(f"Music changed: {name}")

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

            self.frame_index += 1
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
                self.play_sound("pants")
                self.pants_on = False
            elif key == pygame.K_2 and len(options) > 1:
                self.selected_clothes = options[1]
                self.stage = Stage.LEVEL_SELECT
                self.play_sound("diapers")
                self.diaper_on = False
                self.pants_on = False

        elif self.stage == Stage.LEVEL_SELECT:
            if key in (pygame.K_1, pygame.K_2):
                self.selected_level = LEVELS[0]
                self.stage = Stage.PLAYING
                self.play_sound("ready_go_poo")

        elif self.stage == Stage.PLAYING:
            self.handle_playing_keys(key)

        elif self.stage == Stage.COMPLETE and key == pygame.K_r:
            self.__init__()

    def handle_playing_keys(self, key: int) -> None:
        if key == pygame.K_SPACE:
            self.advance_sequence()
            return
        if key == pygame.K_m:
            self.cycle_music()
            return

        key_name = pygame.key.name(key).upper()
        sound_key = MANUAL_SOUND_KEYS.get(key_name)
        if sound_key:
            self.play_sound(sound_key)
            self.log.append(f"Manual sound: {sound_key}")

    def advance_sequence(self) -> None:
        step = MEGA_STEPS[self.script_index]
        self.log.append(step["text"])
        self.play_sound(step["sound"])
        self.current_emotion = self.infer_emotion(step["text"], step["sound"])
        self.play_emotion_layer()

        self.defecate_count += step["defecate"]
        self.fart_count += step["fart"]
        self.pee_count += step["pee"]

        self.target_index = (self.target_index + 1) % len(TARGET_ITEMS)
        self.current_target = TARGET_ITEMS[self.target_index]
        self.play_item_sound()
        self.script_index += 1

        if self.script_index >= len(MEGA_STEPS):
            self.log.extend(COMPLETION_MESSAGES)
            self.stage = Stage.COMPLETE

    def infer_emotion(self, text: str, sound: str) -> str:
        merged = f"{text.lower()} {sound.lower()}"
        if "ready" in merged or "yaaay" in merged or "did it" in merged:
            return "super_happy"
        if "sad" in merged or "ahh" in merged:
            return "sad"
        if "angry" in merged:
            return "angry"
        if "scared" in merged:
            return "scared"
        if "push" in merged or "fart" in merged or "defecate" in merged or "eeee" in merged or "ehhhh" in merged:
            return "pushing"
        return "happy"

    def draw_background(self) -> None:
        top = BACKGROUND_COLORS["top"]
        bottom = BACKGROUND_COLORS["bottom"]
        for y in range(760):
            t = y / 759
            color = (
                int(top[0] * (1 - t) + bottom[0] * t),
                int(top[1] * (1 - t) + bottom[1] * t),
                int(top[2] * (1 - t) + bottom[2] * t),
            )
            pygame.draw.line(self.screen, color, (0, y), (1280, y))

        bubble = BACKGROUND_COLORS["bubble"]
        for i in range(12):
            x = (i * 111 + self.frame_index * (i + 1)) % 1280
            y = 730 - ((self.frame_index * (i + 2)) % 760)
            r = 8 + (i % 6)
            pygame.draw.circle(self.screen, bubble, (x, y), r, width=2)

    def draw(self) -> None:
        self.draw_background()
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
        title = self.big_font.render("UNPOTTY DELUXE VERSION 2 SUPER MEGA COLLECTION", True, (255, 238, 120))
        self.screen.blit(title, (40, 18))

    def draw_character_preview(self, x: int = 920, y: int = 150, final_pose: bool = False) -> None:
        sprite = render_character_pose(
            character=self.selected_character,
            emotion=self.current_emotion,
            shirt_on=self.shirt_on,
            pants_on=self.pants_on,
            diaper_on=self.diaper_on,
            hold_toilet_paper=final_pose,
        )
        self.screen.blit(sprite, (x, y))

    def draw_character_select(self) -> None:
        t = self.font.render("Select Character: [1] Toddler  [2] Kid", True, (230, 230, 240))
        self.screen.blit(t, (60, 108))
        t2 = self.small.render("AI generated sprites + sounds + background enabled.", True, (180, 210, 255))
        self.screen.blit(t2, (60, 148))
        self.draw_character_preview()

    def draw_clothes_select(self) -> None:
        options = CHARACTERS[self.selected_character]["clothing"]
        txt = self.font.render(f"{self.selected_character} selected. Choose clothes action:", True, (230, 230, 240))
        self.screen.blit(txt, (60, 112))
        self.screen.blit(self.small.render(f"[1] {options[0]}", True, (255, 255, 255)), (80, 155))
        self.screen.blit(self.small.render(f"[2] {options[1]}", True, (255, 255, 255)), (80, 186))
        self.draw_character_preview()

    def draw_level_select(self) -> None:
        self.screen.blit(self.font.render("Level Select", True, (230, 230, 240)), (60, 110))
        self.screen.blit(self.small.render("[1] Mega Level Un-Potty  (Press 1 to start)", True, (255, 255, 255)), (80, 154))
        self.draw_character_preview()

    def draw_playing(self) -> None:
        card = pygame.Rect(40, 100, 1200, 610)
        pygame.draw.rect(self.screen, (44, 36, 60), card, border_radius=20)

        self.screen.blit(
            self.small.render(
                f"Character: {self.selected_character} | Clothes: {self.selected_clothes} | Level: {self.selected_level}",
                True,
                (225, 225, 225),
            ),
            (65, 122),
        )
        self.screen.blit(self.small.render(f"Current target item: {self.current_target}", True, (255, 180, 180)), (65, 154))
        item_icon = render_item_icon(self.current_target)
        self.screen.blit(item_icon, (975, 120))
        self.screen.blit(self.small.render(f"Target progress: {self.target_index + 1}/{len(TARGET_ITEMS)}", True, (255, 210, 120)), (65, 184))
        self.screen.blit(
            self.small.render(f"Defecate: {self.defecate_count}   Fart: {self.fart_count}   Pee: {self.pee_count}", True, (170, 255, 170)),
            (65, 218),
        )
        step_left = len(MEGA_STEPS) - self.script_index
        self.screen.blit(self.small.render(f"Press SPACE for next mega V2 step ({step_left} left)", True, (190, 210, 250)), (65, 250))
        controls = "Controls: F/T/S/A/G/P/D/H/R/Y sounds, M music, SPACE next step, auto item tones"
        self.screen.blit(self.small.render(controls, True, (190, 190, 250)), (65, 280))

        recent = self.log[-10:]
        for i, line in enumerate(recent):
            self.screen.blit(self.small.render(f"- {line}", True, (240, 240, 240)), (82, 320 + i * 28))

        self.draw_character_preview(x=940, y=330)

    def draw_complete(self) -> None:
        self.screen.blit(self.big_font.render("UN-POTTY COMPLETED", True, (140, 255, 140)), (300, 160))
        lines = [
            "I did it!! Version 2 complete!",
            "No no clean up / Not clean up.",
            "Ewwww smell completed poo poo. Yaaayyy! Press R to restart.",
        ]
        for i, line in enumerate(lines):
            self.screen.blit(self.font.render(line, True, (230, 230, 240)), (160, 270 + i * 48))
        self.draw_character_preview(x=950, y=300, final_pose=True)


def main() -> None:
    Game().run()


if __name__ == "__main__":
    main()
