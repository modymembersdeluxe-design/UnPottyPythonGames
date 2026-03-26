"""Procedural art/sound helpers for UnPotty Deluxe."""

from __future__ import annotations

import math
import os
import struct
import wave
from pathlib import Path

import pygame

from game_data import SOUND_DESIGN

ASSET_DIR = Path("assets")
SPRITE_DIR = ASSET_DIR / "sprites"
SOUND_DIR = ASSET_DIR / "sounds"


def ensure_dirs() -> None:
    SPRITE_DIR.mkdir(parents=True, exist_ok=True)
    SOUND_DIR.mkdir(parents=True, exist_ok=True)


def _draw_character(surface: pygame.Surface, body_color: tuple[int, int, int], eye_shift: int) -> None:
    surface.fill((0, 0, 0, 0))
    pygame.draw.ellipse(surface, (255, 232, 201), pygame.Rect(52, 34, 136, 112))
    pygame.draw.rect(surface, body_color, pygame.Rect(56, 135, 128, 170), border_radius=28)
    pygame.draw.circle(surface, (22, 22, 22), (95 + eye_shift, 86), 7)
    pygame.draw.circle(surface, (22, 22, 22), (145 + eye_shift, 86), 7)
    pygame.draw.arc(surface, (160, 25, 25), pygame.Rect(86, 103, 72, 32), math.radians(12), math.radians(168), 4)


def generate_character_sprite_frames(name: str, color: tuple[int, int, int]) -> list[Path]:
    ensure_dirs()
    frames: list[Path] = []
    for idx, eye_shift in enumerate((0, -2, 2, 0, -1, 1)):
        surface = pygame.Surface((240, 340), pygame.SRCALPHA)
        _draw_character(surface, color, eye_shift)
        font = pygame.font.SysFont("arial", 30, bold=True)
        txt = font.render(name.upper(), True, (250, 250, 250))
        surface.blit(txt, (38, 292))
        frame_path = SPRITE_DIR / f"{name.lower()}_{idx:02d}.png"
        pygame.image.save(surface, str(frame_path))
        frames.append(frame_path)
    return frames


def generate_tone(path: os.PathLike[str], hz: float, duration: float, vibrato: float = 0.0) -> None:
    ensure_dirs()
    sample_rate = 44100
    amplitude = 11000
    frames = int(sample_rate * duration)

    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(frames):
            t = i / sample_rate
            envelope = 1.0
            if t < 0.03:
                envelope = t / 0.03
            elif t > duration - 0.06:
                envelope = max(0.0, (duration - t) / 0.06)

            mod = 1 + 0.03 * math.sin(2 * math.pi * vibrato * t)
            f0 = hz * mod
            wave_a = math.sin(2 * math.pi * f0 * t)
            wave_b = 0.5 * math.sin(2 * math.pi * f0 * 2.01 * t)
            wave_c = 0.25 * math.sin(2 * math.pi * f0 * 0.51 * t)
            value = int(amplitude * envelope * (wave_a + wave_b + wave_c) / 1.75)
            wav.writeframesraw(struct.pack("<h", value))


def prepare_all_assets() -> dict[str, object]:
    ensure_dirs()
    pygame.font.init()

    sprites = {
        "Toddler": generate_character_sprite_frames("Toddler", (106, 158, 255)),
        "Kid": generate_character_sprite_frames("Kid", (122, 218, 98)),
    }

    sound_paths: dict[str, Path] = {}
    for sound_name, (hz, duration) in SOUND_DESIGN.items():
        path = SOUND_DIR / f"{sound_name}.wav"
        if not path.exists():
            vibrato = 5.0 if hz < 120 else 2.5
            generate_tone(path, hz=hz, duration=duration, vibrato=vibrato)
        sound_paths[sound_name] = path

    return {
        "toddler_frames": sprites["Toddler"],
        "kid_frames": sprites["Kid"],
        "sounds": sound_paths,
    }
