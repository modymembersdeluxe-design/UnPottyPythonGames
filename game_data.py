"""Game data and narrative strings for UnPotty Deluxe Version 2."""

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

LEVELS = ["Mega Level Un-Potty V2"]

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
    "feeling": (220, 1.10),
    "tummy": (176, 1.30),
    "scared": (260, 1.25),
    "sad": (150, 1.25),
    "angry_push": (320, 1.15),
    "pants": (300, 0.55),
    "diapers": (140, 0.70),
    "hands_hole": (190, 1.00),
    "ready_go_poo": (350, 1.25),
    "fart_repeat": (80, 1.70),
    "fart_long_repeat3": (74, 1.45),
    "defecate_wait_ahh": (120, 1.75),
    "scattered_push": (105, 1.55),
    "fart_long": (70, 2.10),
    "pooped_repeat": (95, 1.95),
    "super_pooped_long": (60, 2.60),
    "hole_pooped_x5": (82, 2.20),
    "fart_longest": (52, 3.20),
    "pee_long": (500, 1.50),
    "finally_push_ending": (240, 1.30),
    "i_did_it": (420, 1.40),
    "no_clean_up": (280, 1.10),
    "not_clean_up": (210, 1.15),
    "eww_smell": (66, 1.80),
    "yay_unpotty": (520, 1.60),
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
    "Y": "pee_long",
}

CORE_MEGA_STEPS = [
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
    {"text": "(super pooped long repeat 5 + pee long repeat 5).", "sound": "super_pooped_long", "defecate": 5, "fart": 2, "pee": 5},
    {"text": "(hole pooped x5 on items all more).", "sound": "hole_pooped_x5", "defecate": 5, "fart": 2, "pee": 2},
    {"text": "(finally a fart longest ending onto pooped longest).", "sound": "fart_longest", "defecate": 4, "fart": 6, "pee": 2},
    {"text": "(finally pushing ending).", "sound": "finally_push_ending", "defecate": 1, "fart": 1, "pee": 1},
    {"text": "(I did it!!).", "sound": "i_did_it", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(No no clean up).", "sound": "no_clean_up", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(Not Clean Up).", "sound": "not_clean_up", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(Ewwww smell completed poo poo).", "sound": "eww_smell", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "(yaaayyy!).", "sound": "yay_unpotty", "defecate": 0, "fart": 0, "pee": 0},
]


def build_mega_steps_v2() -> list[dict[str, object]]:
    """Build a long version-2 sequence by combining core script + per-item finale events."""
    steps = list(CORE_MEGA_STEPS)
    for item in TARGET_ITEMS:
        steps.append(
            {
                "text": f"V2 mega item action onto {item}: push, fart long, poop long, pee long.",
                "sound": "pooped_repeat",
                "defecate": 2,
                "fart": 2,
                "pee": 2,
            }
        )
    steps.extend(
        [
            {"text": "V2 ending: well done, great job, unpotty did it.", "sound": "i_did_it", "defecate": 0, "fart": 0, "pee": 0},
            {"text": "V2 smell finale: no clean up, not clean up, ewwwww smell.", "sound": "eww_smell", "defecate": 0, "fart": 0, "pee": 0},
            {"text": "V2 laughing finale: more games unlocked.", "sound": "yay_unpotty", "defecate": 0, "fart": 0, "pee": 0},
        ]
    )
    return steps


MEGA_STEPS = build_mega_steps_v2()

COMPLETION_MESSAGES = [
    "UN-POTTY COMPLETED VERSION 2",
    "No clean up mode stayed ON.",
    "(laughing) more games unlocked!",
]
