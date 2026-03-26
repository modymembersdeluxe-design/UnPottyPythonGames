"""Procedural sounds generation for UnPotty Deluxe Version 2."""

from __future__ import annotations

import hashlib
import math
import os
import struct
import wave
from pathlib import Path

from game_data import SOUND_DESIGN, TARGET_ITEMS

ASSET_DIR = Path("assets")
SOUND_DIR = ASSET_DIR / "sounds"
ITEM_SOUND_DIR = SOUND_DIR / "items"

EMOTION_STYLES = {
    "sad": (0.65, 0.20),
    "angry": (1.20, 0.45),
    "scared": (1.05, 0.55),
    "pushing": (1.35, 0.30),
    "super_happy": (1.10, 0.18),
    "happy": (1.00, 0.14),
}


def ensure_sound_dir() -> None:
    SOUND_DIR.mkdir(parents=True, exist_ok=True)
    ITEM_SOUND_DIR.mkdir(parents=True, exist_ok=True)


def generate_tone(path: os.PathLike[str], hz: float, duration: float, vibrato: float = 0.0, grit: float = 0.2) -> None:
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
            wave_d = grit * math.sin(2 * math.pi * f0 * 3.2 * t)
            value = int(amplitude * envelope * (wave_a + wave_b + wave_c + wave_d) / 2.0)
            wav.writeframesraw(struct.pack("<h", value))


def build_all_feature_sounds() -> dict[str, Path]:
    """Regenerate all sound files for the V2 longer sound set."""
    ensure_sound_dir()
    sound_paths: dict[str, Path] = {}
    for sound_name, (hz, duration) in SOUND_DESIGN.items():
        path = SOUND_DIR / f"{sound_name}.wav"
        vibrato = 5.0 if hz < 120 else 2.5
        grit = 0.35 if "fart" in sound_name or "push" in sound_name else 0.2
        generate_tone(path, hz=hz, duration=duration, vibrato=vibrato, grit=grit)
        sound_paths[sound_name] = path
    return sound_paths


def _item_freq(item: str) -> float:
    digest = hashlib.sha256(item.encode()).digest()
    return 160 + (digest[0] + digest[3]) % 420


def build_item_sounds() -> dict[str, Path]:
    ensure_sound_dir()
    out: dict[str, Path] = {}
    for item in TARGET_ITEMS:
        safe = item.replace(" ", "_").replace("-", "_")
        path = ITEM_SOUND_DIR / f"{safe}.wav"
        freq = _item_freq(item)
        generate_tone(path, hz=freq, duration=0.42, vibrato=1.9, grit=0.12)
        out[item] = path
    return out


def build_emotion_layers() -> dict[str, Path]:
    ensure_sound_dir()
    out: dict[str, Path] = {}
    for emotion, (pitch_scale, grit) in EMOTION_STYLES.items():
        path = SOUND_DIR / f"emotion_{emotion}.wav"
        generate_tone(path, hz=210 * pitch_scale, duration=0.75, vibrato=3.2, grit=grit)
        out[emotion] = path
    return out
