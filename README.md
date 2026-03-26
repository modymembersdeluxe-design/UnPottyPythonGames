# UnPotty Python Games - Mega Deluxe Prototype (Version 2)

Updated prototype for **UnPotty Mega Deluxe Time Games V2** with:
- longer animated sprites (`sprite_factory.py`) with emotion + outfit layers
- longer generated feature sound effects (`sounds_factory.py`) + emotion layers + per-item tones
- generated music tracks (`music_factory.py`) including `unpotty_trained`, `unpotty_trainined`, `potty_failed`, `poo_poo_song`
- dynamic background + expanded controls in gameplay
- longest V2 mega sequence that includes core events and per-item mega actions
- runtime character emotion states (sad/angry/scared/pushing/happy) + item icons + toilet-paper finale pose

## Files

- `unpotty_deluxe.py` - game loop, background rendering, controls, sequence logic, V2 flow, emotion/outfit/item rendering
- `game_data.py` - characters, level/items, longest V2 step sequence, sound mappings, control mapping
- `game_date.py` - compatibility export module for requested naming
- `sprite_factory.py` - procedural toddler/kid sprite frames (extended frame cycle)
- `sounds_factory.py` - procedural feature SFX generation (longer tones), emotion layers, and item-specific tones
- `music_factory.py` - procedural music tracks
- `asset_factory.py` - orchestrates sprite, SFX, emotion, item-tone, and music generators

## Run

```bash
python3 -m pip install -r requirements.txt
python3 unpotty_deluxe.py
```

## Gameplay controls

- `1` / `2` select menu options
- `SPACE` next mega step
- `F/T/S/A/G/P/D/H/R/Y` manual feature sound triggers (`Y` = pee long), plus auto emotion/item tones per step
- `M` cycle generated music tracks
- `R` restart on completion
- `ESC` quit

This project is intentionally comedic and exaggerated per request.
