"""Game data and narrative strings for UnPotty Deluxe."""

from __future__ import annotations

CHARACTERS = {
    "Toddler": {
        "description": "Tiny champion, ready for mega un-potty chaos.",
        "clothing": ["Remove pants", "Remove diapers"],
        "sprite_theme": "toddler",
    },
    "Kid": {
        "description": "Big kid with bold tummy rumbles.",
        "clothing": ["Remove pants", "Remove underpants"],
        "sprite_theme": "kid",
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

SOUND_DESIGN = {
    "feeling": (220, 0.95),
    "tummy": (176, 1.10),
    "scared": (260, 1.20),
    "pants": (300, 0.45),
    "diapers": (140, 0.60),
    "hands_hole": (190, 0.80),
    "ready_go_poo": (350, 1.05),
    "fart_repeat": (80, 1.40),
    "defecate_wait": (120, 1.35),
    "ahh_wait": (150, 1.60),
    "scattered_push": (105, 1.25),
    "fart_long": (70, 1.80),
    "pooped_repeat": (95, 1.55),
    "super_pooped_long": (60, 2.10),
    "hole_pooped_x5": (82, 1.90),
    "fart_longest": (52, 2.40),
    "i_did_it": (420, 1.25),
    "no_clean_up": (280, 0.90),
    "eww_smell": (66, 1.50),
    "yay_unpotty": (520, 1.40),
}

MEGA_STEPS = [
    {"text": "Feeling: tummy rumble begins.", "sound": "feeling", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "Tummy feeling stronger... ready to go poo poo!", "sound": "tummy", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "Taking off pants.", "sound": "pants", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "Taking off diapers/underpants.", "sound": "diapers", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "Hands to hole. Let's go ready to go poo poo!", "sound": "hands_hole", "defecate": 1, "fart": 0, "pee": 0},
    {"text": "Hole onto fart repeat 5 and defecate repeat 5.", "sound": "fart_repeat", "defecate": 5, "fart": 5, "pee": 0},
    {"text": "Defecate waiting... ahh feeling...", "sound": "defecate_wait", "defecate": 1, "fart": 1, "pee": 1},
    {"text": "Scared feeling, keep pushing with hands to hole.", "sound": "scared", "defecate": 2, "fart": 1, "pee": 1},
    {"text": "Ehhhhmmmmmahhhhmmmmm... defecate scattered pushing.", "sound": "scattered_push", "defecate": 3, "fart": 1, "pee": 2},
    {"text": "Fart long repeat 5 and pooped repeat.", "sound": "fart_long", "defecate": 3, "fart": 5, "pee": 1},
    {"text": "Super pooped long repeat 5.", "sound": "super_pooped_long", "defecate": 5, "fart": 2, "pee": 3},
    {"text": "Hole pooped x5 onto items all more.", "sound": "hole_pooped_x5", "defecate": 5, "fart": 2, "pee": 2},
    {"text": "Finally a fart longest ending onto pooped longest.", "sound": "fart_longest", "defecate": 4, "fart": 6, "pee": 2},
    {"text": "I did it!! Great job, UnPotty completed.", "sound": "i_did_it", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "No no clean up. Ewwww what's that smell?", "sound": "eww_smell", "defecate": 0, "fart": 0, "pee": 0},
    {"text": "Yaaayyy! More UnPotty games unlocked.", "sound": "yay_unpotty", "defecate": 0, "fart": 0, "pee": 0},
]

COMPLETION_MESSAGES = [
    "UN-POTTY COMPLETED",
    "No clean up mode stayed ON.",
    "(laughing) more games unlocked!",
]
