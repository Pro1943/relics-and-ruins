```
      ▄▄▄▄▄▄         ▄▄                                        ▄▄▄▄▄▄                        
     █▀██▀▀▀█▄        ██                                 █▄   █▀██▀▀▀█▄                      
       ██▄▄▄█▀        ██ ▀▀                     ▄        ██     ██▄▄▄█▀        ▀▀ ▄          
       ██▀▀█▄   ▄█▀█▄ ██ ██ ▄███▀ ▄██▀█   ▄▀▀█▄ ████▄ ▄████     ██▀▀█▄   ██ ██ ██ ████▄ ▄██▀█
     ▄ ██  ██   ██▄█▀ ██ ██ ██    ▀███▄   ▄█▀██ ██ ██ ██ ██   ▄ ██  ██   ██ ██ ██ ██ ██ ▀███▄
     ▀██▀  ▀██▀▄▀█▄▄▄▄██▄██▄▀███▄█▄▄██▀  ▄▀█▄██▄██ ▀█▄█▀███   ▀██▀  ▀██▀▄▀██▀█▄██▄██▄▀██▄▄██▀
```

# 🏺 Relics and Ruins

**Relics and Ruins** is a **turn-based RPG prototype** built in Python, evolving from a CLI experience into a full **GUI-based game using PySide6**.

Explore forgotten ruins, fight corrupted enemies, collect loot, and manage your inventory — all while learning **real-world Python game architecture**.

This project is **open-source**, **learning-focused**, and actively evolving.

---

## 🎮 Game Overview

**Relics and Ruins** features:

* 🗡️ **Turn-Based Combat** — Attack, Defend, or unleash limited-use Specials
* 🤖 **Dynamic Enemy AI** — Enemies attack, defend, miss, or use specials
* 🎒 **Inventory System** — Loot drops, item tracking, and usage
* 💾 **Save & Load** — Inventory persists between sessions
* 🖥️ **GUI + Terminal Support** — PySide6 GUI with CLI roots
* 🎨 **ASCII Art Screens** — Intro, victory, and game-over screens

---

## 🚀 Installation & Running the Game

### 🔹 Option 1: Run the Windows Executable (Recommended)

1. Go to the **Releases** section of this repository
2. Download the latest **v0.2 `.zip`**
3. Extract the archive
4. Run `RelicsAndRuins.exe`

> ⚠️ **Windows SmartScreen Warning**
> The executable is unsigned, so Windows may block it.
> Click **“More info” → “Run anyway”** to launch the game.

✅ No Python installation required.

---

### 🔹 Option 2: Run From Source (Developers / Contributors)

#### Requirements

* **Python 3.8+**
* `pip` installed

#### Steps

```bash
# Clone the repository
git clone https://github.com/Pro1943/relics-and-ruins.git
cd relics-and-ruins

# Install dependencies
pip install -r requirments.txt

# Run the game
python main.py

#For compiling it into an .exe use the following command
pyinstaller --onefile --windowed --name RelicsAndRunes --icon assets/icon/game_icon.ico main.py

#or

python -m PyInstaller --onefile --windowed --name RelicsAndRunes --icon assets/icon/game_icon.ico main.py
```

The game launches in **GUI mode** using **PySide6**.

If PySide6 is missing:

```bash
pip install PySide6
```

---

## 📁 Project Structure

```
relics-and-ruins/
├── main.py                      # Entry point—launches GUI or shows install prompt
├── requirments.txt              # Python dependencies
│
├── core/                        # Game state & logic
│   ├── game_state.py            # Central GameState class (HP, inventory, combat, specials)
│   └── __init__.py
│
├── assets/                      # Game mechanics & data
│   ├── player.py                # Player action helpers
│   ├── enemy.py                 # Enemy logic (damage, defense, special abilities)
│   ├── fighting.py              # Combat resolver (turn handling, events)
│   ├── inventory.py             # Inventory management helpers
│   ├── drops.py                 # Random loot generation
│   ├── loot_table.py            # Item definitions (bones, leather, relics, etc.)
│   ├── battles.py               # Battle initialization
│   ├── interactions.py          # NPC & world interactions
│   ├── item_states.py           # Item state & effects
│   ├── clear_terminal.py        # Terminal utilities
│   └── icon/                    # Game assets & icons
│
├── ui/                          # User interface
│   ├── gui_main.py              # GUI launcher
│   ├── main_window.py           # Main window logic
│   ├── styles.py                # GUI styling
│   └── pages/                   # Individual game screens
│       ├── start_page.py        # Intro/start screen
│       ├── combat_page.py       # Combat interface
│       ├── inventory_page.py    # Inventory Interface
│       ├── intro_page.py        # Intro interface
│       ├── gameover_page.py     # Gameover interface
│       └── victory_page.py      # Victory interface
│
├── saveing/                     # Save & load system
│   ├── save.py                  # Serialize inventory to disk
│   ├── load.py                  # Load inventory from disk
│   └── __init__.py
│
├── CONTRIBUTORS.md              # Team & contribution info
└── LICENSE                      # RRL v1.0 (non-commercial)
```

---

## 🕹️ Gameplay Mechanics

### Combat

**Player Actions**

* **Attack**: 1–19 damage
* **Defend**: +5 defense (next turn)
* **Special**: 20–40 damage (max 4 uses)
* **Inventory**: View/use items

**Enemy Behavior**

* 50%: Normal attack
* 7%: Defend
* 12%: Miss
* 31%: Special attack

Combat ends when either side reaches **0 HP**.

---

### Loot & Inventory

Enemies can drop:

* **Common**: Bone, Leather, Iron Scrap, Berry, Thread
* **Rare**: Relic Shards, Cursed Amulets, Ancient Texts
* **Special**: Potions, armor upgrades, artifacts

Inventory automatically saves after combat.

---

## 🧠 Architecture Philosophy

* **Single Source of Truth** → `GameState`
* **No global state**
* **Logic ≠ UI**
* **Readable code > clever code**
* **Learning over shortcuts**

The game logic is UI-agnostic, making it easy to expand or replace interfaces.

---

## 🛠️ Tech Stack

| Component | Technology              |
| --------- | ----------------------- |
| Language  | Python 3.8+             |
| GUI       | PySide6 (Qt for Python) |
| Terminal  | colorama                |
| Build     | PyInstaller             |

---

## 📋 Current Features (v0.2)

✅ Turn-based combat
✅ Enemy AI
✅ Inventory & loot system
✅ Save/load
✅ GUI interface
✅ ASCII art screens
✅ Special ability limits

---

## 🤝 Contributing

We welcome contributions — bug fixes, features, balance tweaks, UI improvements, and documentation.

### How to Contribute

1. Fork the repository
2. Clone your fork:

   ```bash
   git clone https://github.com/pro1943/relics-and-ruins.git
   cd relics-and-ruins
   ```
3. Commit clearly
4. Push and open a Pull Request

All contributors are credited in **CONTRIBUTORS.md**.

> ⚠️ By contributing, you agree your work is licensed under **RRL v1.0**.

---

## 📜 License

This project is licensed under the **Relics and Ruins License (RRL v1.0)**.

* ✅ Open-source
* ✅ Free to learn, modify, and contribute
* ❌ No commercial use
* ❌ No rebranding or credit removal

See [`LICENSE`](LICENSE) for full terms.

---

## 🏆 Core Team

* **Pro_1943 / Pieater9000** — Founder, core systems, architecture
* **Najesh Afroz Shah** — Co-developer, testing, balancing

---

## ❓ FAQ

**Is this a finished game?**
No — it’s a playable prototype.

**Can I sell this?**
No. Commercial use is forbidden.

**Can I fork it?**
Yes, for learning and non-commercial projects.

**Where do I report bugs?**
Open an issue on GitHub.

---

**The ruins are unstable.
The code is evolving.
Enter at your own risk. 🏺🔥**

---