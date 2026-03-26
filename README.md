# UnPotty Python Games - Mega Deluxe Prototype

Updated prototype for **UnPotty Mega Deluxe Time Games** with longer scripted flow, more generated sounds, and animated generated character sprite frames.

## Included files

- `unpotty_deluxe.py`
  - character selection (Toddler/Kid)
  - clothes-removal selection
  - mega level selection
  - long multi-step “feeling → tummy → scared → push → fart/poop/pee” event chain
  - target-item cycle across the full mega item list
- `game_data.py`
  - character metadata
  - mega target item list
  - sound design map for many feature sounds
  - long `MEGA_STEPS` sequence with per-step counters and sound keys
- `asset_factory.py`
  - procedural animated sprite-frame generation
  - procedural longer synthesized sound generation for all feature sound cues

## Run

```bash
python3 -m pip install -r requirements.txt
python3 unpotty_deluxe.py
```

## Controls

- `1` / `2` select menu options
- `SPACE` advances to the next mega sequence step
- `R` restart after completion
- `ESC` quit

This project is intentionally comedic and exaggerated per request.
