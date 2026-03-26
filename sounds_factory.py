"""Procedural sounds generation for UnPotty Deluxe."""

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


def build_all_feature_sounds() -> dict[str, Path]:
    ensure_sound_dir()
    sound_paths: dict[str, Path] = {}
    for sound_name, (hz, duration) in SOUND_DESIGN.items():
        path = SOUND_DIR / f"{sound_name}.wav"
        if not path.exists():
            vibrato = 5.0 if hz < 120 else 2.5
            generate_tone(path, hz=hz, duration=duration, vibrato=vibrato)
        sound_paths[sound_name] = path
    return sound_paths
