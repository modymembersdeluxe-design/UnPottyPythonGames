"""Procedural art/sound helpers for UnPotty Deluxe."""

from __future__ import annotations

import math
import os
import struct
import wave
from pathlib import Path

import pygame

ASSET_DIR = Path("assets")
SPRITE_DIR = ASSET_DIR / "sprites"
SOUND_DIR = ASSET_DIR / "sounds"


def ensure_dirs() -> None:
    SPRITE_DIR.mkdir(parents=True, exist_ok=True)
    SOUND_DIR.mkdir(parents=True, exist_ok=True)


def generate_character_sprite(name: str, color: tuple[int, int, int]) -> Path:
    ensure_dirs()
    surface = pygame.Surface((200, 240), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))

    pygame.draw.circle(surface, (255, 224, 189), (100, 62), 42)
    pygame.draw.rect(surface, color, pygame.Rect(58, 105, 84, 108), border_radius=22)
    pygame.draw.circle(surface, (15, 15, 15), (85, 58), 5)
    pygame.draw.circle(surface, (15, 15, 15), (115, 58), 5)
    pygame.draw.arc(surface, (140, 30, 30), pygame.Rect(78, 70, 44, 22), math.radians(10), math.radians(170), 3)

    font = pygame.font.SysFont("arial", 24, bold=True)
    txt = font.render(name.upper(), True, (250, 250, 250))
    surface.blit(txt, (16, 208))

    file_path = SPRITE_DIR / f"{name.lower()}_sprite.png"
    pygame.image.save(surface, str(file_path))
    return file_path


def generate_tone(path: os.PathLike[str], hz: float, duration: float) -> None:
    ensure_dirs()
    sample_rate = 44100
    amplitude = 9000
    frames = int(sample_rate * duration)

    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(frames):
            value = int(amplitude * math.sin(2 * math.pi * hz * i / sample_rate))
            wav.writeframesraw(struct.pack("<h", value))


def prepare_all_assets() -> dict[str, Path]:
    ensure_dirs()
    pygame.font.init()
    sprites = {
        "Toddler": generate_character_sprite("Toddler", (106, 158, 255)),
        "Kid": generate_character_sprite("Kid", (122, 218, 98)),
    }
    tones = {
        "fart": SOUND_DIR / "fart.wav",
        "poo": SOUND_DIR / "poo.wav",
        "win": SOUND_DIR / "win.wav",
    }
    if not tones["fart"].exists():
        generate_tone(tones["fart"], 140, 0.18)
    if not tones["poo"].exists():
        generate_tone(tones["poo"], 90, 0.24)
    if not tones["win"].exists():
        generate_tone(tones["win"], 520, 0.30)

    return {
        "toddler_sprite": sprites["Toddler"],
        "kid_sprite": sprites["Kid"],
        "fart": tones["fart"],
        "poo": tones["poo"],
        "win": tones["win"],
    }
