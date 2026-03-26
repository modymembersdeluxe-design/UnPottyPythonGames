"""Game data and narrative strings for UnPotty Deluxe."""

from __future__ import annotations

CHARACTERS = {
    "Toddler": {
        "description": "Tiny champion, ready for mega un-potty chaos.",
        "clothing": ["Remove pants", "Remove diapers"],
    },
    "Kid": {
        "description": "Big kid with bold tummy rumbles.",
        "clothing": ["Remove pants", "Remove underpants"],
    },
}

LEVELS = ["Mega Level Un-Potty"]

TARGET_ITEMS = [
    "bucket", "plate", "bowl", "sink", "cup", "dish", "floor", "sofa",
    "supercomputer", "microcomputer", "laptop", "workstation computer", "digital computer",
    "hard disk drive", "solid state drive", "random access memory", "motherboard", "speaker",
    "keyboard", "mouse", "printer", "xbox one", "playstation 4", "wii", "playstation 3",
    "xbox 360", "gamecube", "playstation 2", "bathtub", "bed", "nightstand", "lamp",
    "dresser", "air-conditioner", "alarm clock", "mobile phone",
]

BACKGROUND_COLORS = {
    "top": (35, 22, 60),
    "bottom": (12, 10, 25),
    "bubble": (120, 90, 180),
}

SOUND_DESIGN = {
    "feeling": (220, 0.95),
    "tummy": (176, 1.10),
    "scared": (260, 1.20),
    "sad": (150, 1.15),
    "angry_push": (320, 1.00),
    "pants": (300, 0.45),
    "diapers": (140, 0.60),
    "hands_hole": (190, 0.80),
    "ready_go_poo": (350, 1.05),
    "fart_repeat": (80, 1.40),
    "fart_long_repeat3": (74, 1.25),
    "defecate_wait_ahh": (120, 1.55),
    "scattered_push": (105, 1.25),
    "fart_long": (70, 1.80),
    "pooped_repeat": (95, 1.55),
    "super_pooped_long": (60, 2.10),
    "hole_pooped_x5": (82, 1.90),
    "fart_longest": (52, 2.40),
    "finally_push_ending": (240, 1.00),
    "i_did_it": (420, 1.25),
    "no_clean_up": (280, 0.90),
    "not_clean_up": (210, 0.95),
    "eww_smell": (66, 1.50),
    "yay_unpotty": (520, 1.40),
}

MANUAL_SOUND_KEYS = {
    "F": "feeling",
    "T": "tummy",
    "S": "scared",
    "A": "sad",
    "G": "angry_push",
    "P": "pants",
    "D": "diapers",
    "H": "hands_hole",
    "R": "ready_go_poo",
}

MEGA_STEPS = [
    {"text": "(feeling) tummy rumble begins.", "sound": "feeling", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(tummy) stronger feeling.", "sound": "tummy", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(scared your feeling) but keep going.", "sound": "scared", "defecate": 0, "fart": 1, "pee": 0},
    {"text": "(taking off pants).", "sound": "pants", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(taking off diapers).", "sound": "diapers", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(taking hands her hole).", "sound": "hands_hole", "defecate": 1, "fart": 0, "pee": 0},
    {"text": "(a ready go poo poo!).", "sound": "ready_go_poo", "defecate": 1, "fart": 1, "pee": 0},
    {"text": "(hole onto fart repeat 5).", "sound": "fart_repeat", "defecate": 5, "fart": 5, "pee": 1},
    {"text": "(hole onto fart longer + defecate waiting + ahh).", "sound": "defecate_wait_ahh", "defecate": 2, "fart": 3, "pee": 1},
    {"text": "(sad your feeling).", "sound": "sad", "defecate": 1, "fart": 1, "pee": 0},
    {"text": "(hole onto fart long repeat 3 waiting defecate hole).", "sound": "fart_long_repeat3", "defecate": 3, "fart": 3, "pee": 1},
    {"text": "(feeling and defecate waiting).", "sound": "feeling", "defecate": 2, "fart": 1, "pee": 1},
    {"text": "(defecate scattered pushing + sad & angry sounds).", "sound": "angry_push", "defecate": 4, "fart": 2, "pee": 2},
    {"text": "ehhhhhhhhhhhhhhhhhhmmmmmmahhhhhhhmmmmm...", "sound": "scattered_push", "defecate": 3, "fart": 2, "pee": 1},
    {"text": "(hands her hole onto fart long repeat 5 + pooped repeat).", "sound": "fart_long", "defecate": 5, "fart": 5, "pee": 2},
    {"text": "(super pooped long repeat 5).", "sound": "super_pooped_long", "defecate": 5, "fart": 2, "pee": 3},
    {"text": "(hole pooped x5 on items all more).", "sound": "hole_pooped_x5", "defecate": 5, "fart": 2, "pee": 2},
    {"text": "(finally a fart longest ending onto pooped longest).", "sound": "fart_longest", "defecate": 4, "fart": 6, "pee": 2},
    {"text": "(finally pushing ending).", "sound": "finally_push_ending", "defecate": 1, "fart": 1, "pee": 1},
    {"text": "(I did it!!).", "sound": "i_did_it", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(No no clean up).", "sound": "no_clean_up", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(Not Clean Up).", "sound": "not_clean_up", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(Ewwww smell completed poo poo).", "sound": "eww_smell", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(yaaayyy!).", "sound": "yay_unpotty", "defecate": 0, "fart": 0, "pee": 0},
]

COMPLETION_MESSAGES = [
    "UN-POTTY COMPLETED",
    "No clean up mode stayed ON.",
    "(laughing) more games unlocked!",
]
