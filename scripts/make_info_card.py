"""Generate the terminal-style profile information card."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")

STATIC = bool(os.environ.get("STATIC"))
WIDTH = 490
HEIGHT = 360
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
TEXT = "#c9d1d9"
MUTED = "#7d8590"
CYAN = "#22d3ee"
GREEN = "#39d353"
GOLD = "#f2cc60"

rows = [
    ("Role", "Software Engineer", CYAN),
    ("Focus", "Cloud, data, and developer tools", TEXT),
    ("Stack", "Python  |  Java  |  Azure  |  SQL", GREEN),
    ("Learning", "Distributed systems and AI", GOLD),
]

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
    f'viewBox="0 0 {WIDTH} {HEIGHT}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>'
    '</linearGradient></defs>',
    f'<rect width="{WIDTH}" height="{HEIGHT}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{WIDTH-1}" height="{HEIGHT-1}" rx="12" '
    f'fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="30" x2="{WIDTH}" y2="30" stroke="{FRAME}"/>',
]

for i, color in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{22 + i * 16}" cy="15" r="5" fill="{color}"/>')
parts.append(f'<text x="{WIDTH / 2}" y="19" fill="{MUTED}" font-size="12" text-anchor="middle">'
             'avi@github:~$ neofetch</text>')
parts.append(f'<text x="28" y="68" fill="{CYAN}" font-size="18" font-weight="700">Animesh2473</text>')
parts.append(f'<text x="28" y="92" fill="{MUTED}" font-size="12">building useful things, one commit at a time</text>')

for index, (label, value, color) in enumerate(rows):
    y = 140 + index * 42
    delay = index * 0.16
    animation = "" if STATIC else f' opacity="0" style="animation: fade-in .45s ease {delay:.2f}s forwards"'
    parts.append(f'<text x="28" y="{y}" font-size="13"{animation}>'
                 f'<tspan fill="{MUTED}">{label:10}</tspan>'
                 f'<tspan fill="{color}">{value}</tspan></text>')

parts.extend([
    f'<line x1="28" y1="322" x2="{WIDTH - 28}" y2="322" stroke="{FRAME}"/>',
    f'<text x="28" y="345" fill="{MUTED}" font-size="11">status</text>',
    f'<text x="{WIDTH - 28}" y="345" fill="{GREEN}" font-size="11" text-anchor="end">available for interesting problems</text>',
])

if not STATIC:
    parts.insert(1, '<style>@keyframes fade-in { from { opacity: 0; transform: translateY(5px); } '
                    'to { opacity: 1; transform: translateY(0); } }</style>')

parts.append('</svg>')
with open(OUT, "w", encoding="utf-8") as output:
    output.write("".join(parts))
print("wrote", OUT)