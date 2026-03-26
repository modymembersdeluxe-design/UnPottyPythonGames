"""Procedural sprite generation for UnPotty Deluxe characters (Version 2)."""

from __future__ import annotations

import math
from pathlib import Path

import pygame

ASSET_DIR = Path("assets")
SPRITE_DIR = ASSET_DIR / "sprites"

EMOTION_COLORS = {
    "happy": (90, 220, 140),
    "super_happy": (255, 230, 90),
    "sad": (110, 150, 255),
    "angry": (255, 110, 110),
    "scared": (190, 140, 255),
    "pushing": (255, 165, 80),
    "neutral": (150, 170, 255),
}


def ensure_sprite_dir() -> None:
    SPRITE_DIR.mkdir(parents=True, exist_ok=True)


def _draw_character(surface: pygame.Surface, body_color: tuple[int, int, int], eye_shift: int, mood: int, aura_color: tuple[int, int, int]) -> None:
    mouth_h = 22 + mood
    surface.fill((0, 0, 0, 0))
    pygame.draw.circle(surface, aura_color, (120, 170), 110, width=4)
    pygame.draw.ellipse(surface, (255, 232, 201), pygame.Rect(52, 34, 136, 112))
    pygame.draw.rect(surface, body_color, pygame.Rect(56, 135, 128, 170), border_radius=28)
    pygame.draw.circle(surface, (22, 22, 22), (95 + eye_shift, 86), 7)
    pygame.draw.circle(surface, (22, 22, 22), (145 + eye_shift, 86), 7)
    pygame.draw.arc(surface, (160, 25, 25), pygame.Rect(86, 103, 72, mouth_h), math.radians(12), math.radians(168), 4)


def generate_character_sprite_frames(name: str, color: tuple[int, int, int]) -> list[Path]:
    ensure_sprite_dir()
    frames: list[Path] = []
    pattern = [
        (0, 0, (80, 120, 255)), (-2, 3, (120, 90, 220)), (2, 6, (230, 120, 120)), (0, -2, (80, 220, 160)),
        (-1, 5, (255, 180, 80)), (1, 8, (255, 120, 80)), (0, 2, (150, 100, 255)), (2, 10, (120, 220, 180)),
        (-3, 4, (240, 140, 120)), (3, 11, (255, 90, 90)), (0, 1, (160, 120, 240)), (1, 7, (120, 210, 210)),
        (-1, 9, (230, 210, 110)), (2, 5, (200, 130, 250)), (0, 12, (255, 100, 140)), (-2, 2, (90, 170, 255)),
    ]

    for idx, (eye_shift, mood, aura) in enumerate(pattern):
        surface = pygame.Surface((240, 340), pygame.SRCALPHA)
        _draw_character(surface, color, eye_shift, mood, aura)
        font = pygame.font.SysFont("arial", 22, bold=True)
        txt = font.render(f"{name.upper()} V2", True, (250, 250, 250))
        surface.blit(txt, (36, 286))
        badge = font.render(f"FRAME {idx+1:02d}", True, (240, 240, 120))
        surface.blit(badge, (48, 310))
        frame_path = SPRITE_DIR / f"{name.lower()}_v2_{idx:02d}.png"
        pygame.image.save(surface, str(frame_path))
        frames.append(frame_path)
    return frames


def render_character_pose(
    character: str,
    emotion: str,
    shirt_on: bool,
    pants_on: bool,
    diaper_on: bool,
    hold_toilet_paper: bool = False,
) -> pygame.Surface:
    """Runtime pose sprite with emotion + outfit layers (family-friendly, no nudity)."""
    surface = pygame.Surface((260, 360), pygame.SRCALPHA)
    aura = EMOTION_COLORS.get(emotion, EMOTION_COLORS["neutral"])
    body = (106, 158, 255) if character == "Toddler" else (122, 218, 98)

    _draw_character(surface, body, 0, 7 if emotion == "pushing" else 2, aura)

    # Shirt layer.
    if shirt_on:
        pygame.draw.rect(surface, (245, 245, 255), pygame.Rect(70, 140, 100, 85), border_radius=16)
    # Pants/diaper layers.
    if pants_on:
        pygame.draw.rect(surface, (60, 80, 150), pygame.Rect(72, 220, 96, 66), border_radius=14)
    elif diaper_on:
        pygame.draw.rect(surface, (245, 245, 245), pygame.Rect(72, 220, 96, 66), border_radius=14)
        pygame.draw.line(surface, (150, 170, 220), (80, 240), (160, 240), 3)
    else:
        # Safe fallback "shorts" layer when both are off.
        pygame.draw.rect(surface, (90, 90, 90), pygame.Rect(74, 220, 92, 52), border_radius=12)

    if hold_toilet_paper:
        pygame.draw.circle(surface, (245, 245, 245), (192, 220), 22)
        pygame.draw.circle(surface, (200, 200, 200), (192, 220), 8)

    font = pygame.font.SysFont("arial", 20, bold=True)
    label = font.render(f"{character} | {emotion}", True, (250, 250, 250))
    surface.blit(label, (20, 328))
    return surface


def render_item_icon(item_name: str) -> pygame.Surface:
    surface = pygame.Surface((170, 54), pygame.SRCALPHA)
    pygame.draw.rect(surface, (66, 52, 92), pygame.Rect(0, 0, 170, 54), border_radius=12)
    pygame.draw.rect(surface, (170, 140, 220), pygame.Rect(2, 2, 166, 50), 2, border_radius=12)
    font = pygame.font.SysFont("arial", 16, bold=True)
    txt = font.render(item_name[:18], True, (245, 245, 245))
    surface.blit(txt, (10, 18))
    return surface
