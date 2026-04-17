import os
import json

# -----------------------------
# 1. Folder structure
# -----------------------------
BASE = "vercel_dist"
PAGES = os.path.join(BASE, "pages")
MODELS = os.path.join(BASE, "models", "fighters")

os.makedirs(PAGES, exist_ok=True)
os.makedirs(MODELS, exist_ok=True)

# -----------------------------
# 2. game.html (full UI)
# -----------------------------
GAME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>DancePlanet Fighter Select</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
/* (CSS removed for brevity in this script version)
   Use the full game.html I generated earlier.
   Paste the full CSS+HTML here if you want the complete file.
*/
</style>
<script src="https://unpkg.com/three@0.160.0/build/three.min.js"></script>
<script src="https://unpkg.com/three@0.160.0/examples/js/controls/OrbitControls.js"></script>
<script src="https://unpkg.com/three@0.160.0/examples/js/loaders/GLTFLoader.js"></script>
</head>
<body>
<h1>DancePlanet Fighter Select</h1>
<p>This is a placeholder. Replace with full game.html content.</p>
</body>
</html>
"""

with open(os.path.join(PAGES, "game.html"), "w", encoding="utf-8") as f:
    f.write(GAME_HTML)

# -----------------------------
# 3. fighter_lore.json
# -----------------------------
FIGHTER_LORE = {
    "fighters": [
        {
            "id": "cyber_dance_warrior",
            "name": "Cyber Dance Warrior",
            "styleLabel": "Neon Rhythm Assault",
            "colorAccent": "#00e5ff",
            "stats": {"style": 9, "power": 7, "speed": 8, "groove": 10},
            "tags": ["Neon", "Combo-heavy", "Crowd Control"],
            "signatureMoves": [
                "Neon Spiral Break",
                "Cyberstep Barrage",
                "Bassline Overdrive"
            ],
            "stageAffinity": "Thrives on neon city rooftops and glitchy cyberspace arenas.",
            "playstyleTips": "Chain long rhythm-based combos and keep the pressure high."
        },
        {
            "id": "street_dance_brawler",
            "name": "Street Dance Brawler",
            "styleLabel": "Concrete Groove Beatdown",
            "colorAccent": "#ff9800",
            "stats": {"style": 7, "power": 9, "speed": 7, "groove": 8},
            "tags": ["Brawler", "Close-range", "Armor"],
            "signatureMoves": [
                "Back Alley Beatdown",
                "Boom Bap Uppercut",
                "Sidewalk Slam Shuffle"
            ],
            "stageAffinity": "Dominates on street corners and underground battle circles.",
            "playstyleTips": "Get in close and stay there."
        },
        {
            "id": "electro_samurai",
            "name": "Electro Samurai",
            "styleLabel": "Blade Groove Precision",
            "colorAccent": "#ff4081",
            "stats": {"style": 8, "power": 8, "speed": 9, "groove": 7},
            "tags": ["Precision", "Whiff Punish", "Mid-range"],
            "signatureMoves": [
                "Voltage Draw Cut",
                "Beat-Synced Iaido",
                "Thunderstep Cross Slash"
            ],
            "stageAffinity": "Excels in neon temples and synthwave shrines.",
            "playstyleTips": "Play patient and reactive."
        },
        {
            "id": "pop_idol_fighter",
            "name": "Pop Idol Fighter",
            "styleLabel": "Spotlight Combo Star",
            "colorAccent": "#ff80ab",
            "stats": {"style": 10, "power": 6, "speed": 8, "groove": 9},
            "tags": ["Showtime", "Mixups", "Crowd Buffs"],
            "signatureMoves": [
                "Encore Spin Kick",
                "Spotlight Step Feint",
                "Chorus Line Launcher"
            ],
            "stageAffinity": "Shines brightest on big stages.",
            "playstyleTips": "Use feints and mixups."
        },
        {
            "id": "robot_groove_unit",
            "name": "Robot Groove Unit",
            "styleLabel": "Mechanical Beat Precision",
            "colorAccent": "#b2ff59",
            "stats": {"style": 6, "power": 8, "speed": 6, "groove": 9},
            "tags": ["Rhythm Perfect", "Zoning", "Setplay"],
            "signatureMoves": [
                "Metronome Missile",
                "Beat Grid Barrier",
                "Syncopated Slam"
            ],
            "stageAffinity": "Controls industrial arenas.",
            "playstyleTips": "Control space with precise timing."
        }
    ]
}

with open(os.path.join(MODELS, "fighter_lore.json"), "w", encoding="utf-8") as f:
    json.dump(FIGHTER_LORE, f, indent=2)

# -----------------------------
# 4. Placeholder GLB files
# -----------------------------
GLB_NAMES = [
    "cyber_dance_warrior.glb",
    "street_dance_brawler.glb",
    "electro_samurai.glb",
    "pop_idol_fighter.glb",
    "robot_groove_unit.glb"
]

for name in GLB_NAMES:
    path = os.path.join(MODELS, name)
    with open(path, "wb") as f:
        f.write(b"glTF")  # minimal placeholder so Vercel stops 404 errors

# -----------------------------
# 5. Optional index.html redirect
# -----------------------------
INDEX_HTML = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0; url=/pages/game.html">
<title>Redirecting…</title>
</head>
<body>
Redirecting to <a href="/pages/game.html">game.html</a>
</body>
</html>
"""

with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)

print("✔ vercel_dist build generated successfully.")
