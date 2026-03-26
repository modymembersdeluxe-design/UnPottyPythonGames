"""Procedural background music clips for UnPotty Deluxe Version 2."""

from __future__ import annotations

import math
import struct
import wave
from pathlib import Path

ASSET_DIR = Path("assets")
MUSIC_DIR = ASSET_DIR / "music"


def ensure_music_dir() -> None:
    MUSIC_DIR.mkdir(parents=True, exist_ok=True)


def _write_song(path: Path, notes: list[tuple[float, float]], bpm: int = 120) -> None:
    sample_rate = 44100
    amplitude = 9000
    beat = 60 / bpm
    frames = []

    for freq, beats in notes:
        length = beats * beat
        total = int(sample_rate * length)
        for i in range(total):
            t = i / sample_rate
            envelope = min(1.0, i / max(1, int(sample_rate * 0.01)))
            if t > length - 0.08:
                envelope *= max(0.0, (length - t) / 0.08)
            tone = math.sin(2 * math.pi * freq * t) + 0.35 * math.sin(2 * math.pi * freq * 2 * t)
            frames.append(int(amplitude * envelope * tone / 1.35))

    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for v in frames:
            wav.writeframesraw(struct.pack("<h", v))


def prepare_music_tracks() -> dict[str, Path]:
    ensure_music_dir()
    tracks = {
        "unpotty_trained": MUSIC_DIR / "unpotty_trained.wav",
        "unpotty_trainined": MUSIC_DIR / "unpotty_trainined.wav",
        "potty_failed": MUSIC_DIR / "potty_failed.wav",
        "poo_poo_song": MUSIC_DIR / "poo_poo_song.wav",
    }
    _write_song(tracks["unpotty_trained"], [(262, 1), (330, 1), (392, 1), (523, 2), (587, 1), (659, 1)], bpm=128)
    _write_song(tracks["unpotty_trainined"], [(262, 1), (392, 1), (494, 1), (523, 2), (659, 1), (784, 1)], bpm=132)
    _write_song(tracks["potty_failed"], [(220, 1), (196, 1), (175, 2), (147, 2)], bpm=90)
    _write_song(tracks["poo_poo_song"], [(294, 0.5), (330, 0.5), (349, 1), (392, 1), (330, 1), (294, 1), (440, 1)], bpm=140)
    return tracks
