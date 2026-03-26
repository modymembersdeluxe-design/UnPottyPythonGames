"""Procedural sprite generation for UnPotty Deluxe characters."""

from __future__ import annotations

import math
from pathlib import Path

import pygame

ASSET_DIR = Path("assets")
SPRITE_DIR = ASSET_DIR / "sprites"


def ensure_sprite_dir() -> None:
    SPRITE_DIR.mkdir(parents=True, exist_ok=True)


def _draw_character(surface: pygame.Surface, body_color: tuple[int, int, int], eye_shift: int, mood: int) -> None:
    mouth_h = 22 + mood
    surface.fill((0, 0, 0, 0))
    pygame.draw.ellipse(surface, (255, 232, 201), pygame.Rect(52, 34, 136, 112))
    pygame.draw.rect(surface, body_color, pygame.Rect(56, 135, 128, 170), border_radius=28)
    pygame.draw.circle(surface, (22, 22, 22), (95 + eye_shift, 86), 7)
    pygame.draw.circle(surface, (22, 22, 22), (145 + eye_shift, 86), 7)
    pygame.draw.arc(surface, (160, 25, 25), pygame.Rect(86, 103, 72, mouth_h), math.radians(12), math.radians(168), 4)


def generate_character_sprite_frames(name: str, color: tuple[int, int, int]) -> list[Path]:
    ensure_sprite_dir()
    frames: list[Path] = []
    pattern = [(0, 0), (-2, 3), (2, 6), (0, -2), (-1, 5), (1, 8), (0, 2), (2, 10)]

    for idx, (eye_shift, mood) in enumerate(pattern):
        surface = pygame.Surface((240, 340), pygame.SRCALPHA)
        _draw_character(surface, color, eye_shift, mood)
        font = pygame.font.SysFont("arial", 30, bold=True)
        txt = font.render(name.upper(), True, (250, 250, 250))
        surface.blit(txt, (38, 292))
        frame_path = SPRITE_DIR / f"{name.lower()}_{idx:02d}.png"
        pygame.image.save(surface, str(frame_path))
        frames.append(frame_path)
    return frames
