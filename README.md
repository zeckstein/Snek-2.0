# Make a new version of the Snek game
Goal: Make a new version of the Snek game that shows better organization, code quality, and use of Python/Pygame features.  
Considering the following:
 - Sound (✔️)
 - Persistent Scoreboard
 - Resizable window and graphics
 - Curve piece?
 - Animation on eat and grow (apple bump travels to end of snake)
 - Two player mode
 - AI mode
 - Power-ups
 - Different game modes

## Requirements
- Python>=3.11
- Pygame>=2.5.2


Project Organization
------------

    ├── README.md          <- The top-level README for this project.
    │
    ├── app.py             <- Entry point. Run this to start the game.
    │
    ├── config.py          <- global config file (minimum window size, default FPS)
    │
    ├── utils.py           <- load_image(), Color: Enum
    │
    ├── zOLD.py            <- previous code base (early learnings)
    │
    ├── assets
    │   ├── images         <- snake and apple .pngs
    │   └── sounds         <- music and sound effects
    │       ├── bg_music   <- background music files (mp3)
    │       └── sfx        <- sound effects
    │
    ├── classes
    │   ├── elements       <- UI elements (buttons, text)
    │   └── objects        <- game objects (snake, apple)
    │
    ├─ scenes             <- Loops for each scene space
    │   ├── main_menu.py
    │   ├── play_Snek.py
    │   ├── options_menu.py    
    │   ├── (#TODO) game_over.py
    │   └── (#TODO) leaderboard.py
    │
    └── .gitignore        <- cache files and .vscode workspace settings (e.g. spellcheck, etc.)