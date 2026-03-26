"""Procedural sounds generation for UnPotty Deluxe Version 2."""

from __future__ import annotations

import math
import os
import struct
import wave
from pathlib import Path

from game_data import SOUND_DESIGN

ASSET_DIR = Path("assets")
SOUND_DIR = ASSET_DIR / "sounds"


def ensure_sound_dir() -> None:
    SOUND_DIR.mkdir(parents=True, exist_ok=True)


def generate_tone(path: os.PathLike[str], hz: float, duration: float, vibrato: float = 0.0) -> None:
    ensure_sound_dir()
    sample_rate = 44100
    amplitude = 11500
    frames = int(sample_rate * duration)

    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(frames):
            t = i / sample_rate
            envelope = 1.0
            attack = 0.04
            release = 0.09
            if t < attack:
                envelope = t / attack
            elif t > duration - release:
                envelope = max(0.0, (duration - t) / release)

            mod = 1 + 0.04 * math.sin(2 * math.pi * vibrato * t)
            f0 = hz * mod
            wave_a = math.sin(2 * math.pi * f0 * t)
            wave_b = 0.55 * math.sin(2 * math.pi * f0 * 2.03 * t)
            wave_c = 0.30 * math.sin(2 * math.pi * f0 * 0.49 * t)
            wave_d = 0.15 * math.sin(2 * math.pi * f0 * 3.2 * t)
            value = int(amplitude * envelope * (wave_a + wave_b + wave_c + wave_d) / 2.0)
            wav.writeframesraw(struct.pack("<h", value))


def build_all_feature_sounds() -> dict[str, Path]:
    """Regenerate all sound files for the V2 longer sound set."""
    ensure_sound_dir()
    sound_paths: dict[str, Path] = {}
    for sound_name, (hz, duration) in SOUND_DESIGN.items():
        path = SOUND_DIR / f"{sound_name}.wav"
        vibrato = 5.0 if hz < 120 else 2.5
        generate_tone(path, hz=hz, duration=duration, vibrato=vibrato)
        sound_paths[sound_name] = path
    return sound_paths
