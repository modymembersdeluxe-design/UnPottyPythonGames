"""Asset orchestrator for UnPotty Deluxe."""

from __future__ import annotations

import pygame

from music_factory import prepare_music_tracks
from sounds_factory import build_all_feature_sounds, build_emotion_layers, build_item_sounds
from sprite_factory import generate_character_sprite_frames


def prepare_all_assets() -> dict[str, object]:
    pygame.font.init()
    sprites = {
        "Toddler": generate_character_sprite_frames("Toddler", (106, 158, 255)),
        "Kid": generate_character_sprite_frames("Kid", (122, 218, 98)),
    }
    sounds = build_all_feature_sounds()
    emotion_layers = build_emotion_layers()
    item_sounds = build_item_sounds()
    music = prepare_music_tracks()
    return {
        "toddler_frames": sprites["Toddler"],
        "kid_frames": sprites["Kid"],
        "sounds": sounds,
        "emotion_layers": emotion_layers,
        "item_sounds": item_sounds,
        "music": music,
    }
