# UnPotty Python Games - Mega Deluxe Prototype

Updated prototype for **UnPotty Mega Deluxe Time Games** with:
- generated animated sprites (`sprite_factory.py`)
- generated feature sound effects (`sounds_factory.py`)
- generated music tracks (`music_factory.py`)
- dynamic background + expanded controls in gameplay

## Files

- `unpotty_deluxe.py` - game loop, screens, background rendering, controls, sequence logic
- `game_data.py` - characters, level/items, long step sequence, sound mappings, control mapping
- `game_date.py` - compatibility export module for requested naming
- `sprite_factory.py` - procedural toddler/kid sprite frames
- `sounds_factory.py` - procedural feature SFX generation
- `music_factory.py` - procedural music tracks (`unpotty_trained`, `potty_failed`, `poo_poo_song`)
- `asset_factory.py` - orchestrates all generators

## Run

```bash
python3 -m pip install -r requirements.txt
python3 unpotty_deluxe.py
```

## Gameplay controls

- `1` / `2` select menu options
- `SPACE` next mega step
- `F/T/S/A/G/P/D/H/R` manual feature sound triggers
- `M` cycle generated music tracks
- `R` restart on completion
- `ESC` quit

This project is intentionally comedic and exaggerated per request.
