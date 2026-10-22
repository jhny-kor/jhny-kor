"""Build the profile's own SVG artwork using only the Python standard library."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'profile'
THEMES = {
    'light': dict(bg='#f6f8fa', panel='#ffffff', ink='#1f2328', muted='#59636e', border='#d1d9e0', green='#168343', blue='#0969da'),
    'dark': dict(bg='#0d1117', panel='#151b23', ink='#f0f6fc', muted='#a4afbd', border='#303b48', green='#3fb950', blue='#58a6ff'),
}
PROJECTS = [
    ('koda', 'KODA', 'Security & quality', ['Local scans for code, dependencies', 'and host posture across platforms.'], ['Python', 'Swift', 'Security'], 'shield'),
    ('koda-mcp', 'KODA-MCP', 'Security for development', ['Security advice for changed text files', 'in closed-network development.'], ['MCP', 'Python', 'Offline'], 'code'),
    ('owntology', 'OWNtology-Kit', 'Personal knowledge', ['Collect personal records into a', 'local knowledge vault on your Mac.'], ['macOS', 'Python', 'Knowledge'], 'nodes'),
    ('remotecontrol', 'RemoteControl', 'Project automation', ['Operate local projects through', 'Telegram and Codex.'], ['Automation', 'Python', 'Telegram'], 'terminal'),
    ('pii-cleaner', 'PII-Cleaner', 'Privacy tools', ['Create separate de-identified copies', 'of text and documents, offline.'], ['Windows', 'Python', 'Privacy'], 'document'),
    ('porta', 'porta', 'Apple apps', ['Screen sharing across Apple devices.', 'Public support & privacy pages.'], ['iOS', 'macOS', 'Swift'], 'devices'),
]


def icon(kind, x, y, color):
    paths = {
        'shield': '<path d="M16 2 29 7v10c0 9-13 15-13 15S3 26 3 17V7Z"/><path d="m10 16 4 4 8-9"/>',
        'code': '<path d="m11 7-8 9 8 9m10-18 8 9-8 9M18 3l-4 26"/>',
        'nodes': '<path d="m7 8 19 3M7 8l8 19m11-16-11 16"/><circle cx="7" cy="8" r="4"/><circle cx="26" cy="11" r="4"/><circle cx="15" cy="27" r="4"/>',
        'terminal': '<rect x="2" y="4" width="29" height="25" rx="4"/><path d="m8 12 5 5-5 5m9 0h7"/>',
        'document': '<path d="M7 2h14l6 6v22H7Z"/><path d="M21 2v7h6M12 15h10m-10 5h10m-10 5h6"/>',
        'devices': '<rect x="1" y="3" width="23" height="18" rx="3"/><path d="M7 27h13m-7-6v6"/><rect x="23" y="12" width="9" height="18" rx="2"/>',
    }
    return f'<g transform="translate({x} {y})" fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths[kind]}</g>'


def svg(width, height, title, body, theme):
    t = THEMES[theme]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}">
  <title>{escape(title)}</title>
  <style>text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}}.ink{{fill:{t['ink']}}}.muted{{fill:{t['muted']}}}.flow{{stroke-dasharray:5 10;animation:flow 7s linear infinite}}@keyframes flow{{to{{stroke-dashoffset:-90}}}}@media(prefers-reduced-motion:reduce){{.flow{{animation:none}}}}</style>
  {body}
</svg>
'''


def hero(theme):
    t = THEMES[theme]
    body = f'''<rect x=".5" y=".5" width="999" height="267" rx="20" fill="{t['bg']}" stroke="{t['border']}"/>
  <path d="M32 39h25" stroke="{t['green']}" stroke-width="3" stroke-linecap="round"/>
  <text x="68" y="44" class="muted" font-size="13" letter-spacing="2">JHNY-KOR / BUILDER</text>
  <text x="32" y="124" class="ink" font-size="66" font-weight="750" letter-spacing="-3">jhny</text>
  <text x="34" y="164" class="ink" font-size="23" font-weight="550">Security. Knowledge. Useful software.</text>
  <text x="34" y="198" class="muted" font-size="15">Building local tools that solve everyday problems.</text>
  <text x="34" y="236" class="muted" font-size="12" letter-spacing="1">SEOUL  ·  PYTHON  /  SWIFT  /  TYPESCRIPT</text>
  <g fill="none" stroke="{t['border']}" stroke-width="1.5">
    <path d="M685 78C823 78 742 190 870 190"/>
    <path d="M872 78C737 78 810 190 685 190"/>
    <path d="M685 78v112M872 78v112"/>
  </g>
  <g fill="none" stroke-width="2.2">
    <path class="flow" d="M685 78C823 78 742 190 870 190" stroke="{t['green']}"/>
    <path class="flow" d="M872 78C737 78 810 190 685 190" stroke="{t['blue']}"/>
  </g>'''
    for x, y, label, kind, color in [
        (615, 43, 'SECURITY', 'shield', t['green']),
        (802, 43, 'KNOWLEDGE', 'nodes', t['blue']),
        (615, 155, 'AUTOMATION', 'terminal', t['blue']),
        (802, 155, 'APPLE APPS', 'devices', t['green']),
    ]:
        body += f'<rect x="{x}" y="{y}" width="140" height="70" rx="12" fill="{t["panel"]}" stroke="{t["border"]}"/>'
        body += icon(kind, x + 12, y + 10, color)
        body += f'<text x="{x+12}" y="{y+56}" class="ink" font-size="10.5" font-weight="600" letter-spacing=".6">{label}</text>'
    return svg(1000, 268, 'jhny — security, knowledge, automation and Apple apps', body, theme)


def card(project, theme):
    slug, name, category, lines, tags, kind = project
    t = THEMES[theme]
    body = f'''<rect x=".5" y=".5" width="439" height="207" rx="16" fill="{t['panel']}" stroke="{t['border']}"/>
  <path d="M23 24h18" stroke="{t['green']}" stroke-width="3" stroke-linecap="round"/>
  <text x="52" y="28" class="muted" font-size="11" letter-spacing=".6">{escape(category.upper())}</text>
  <text x="22" y="75" class="ink" font-size="29" font-weight="700" letter-spacing="-.6">{escape(name)}</text>
  {icon(kind, 383, 44, t['green'])}
  <text x="23" y="109" class="muted" font-size="15">{escape(lines[0])}</text>
  <text x="23" y="132" class="muted" font-size="15">{escape(lines[1])}</text>'''
    x = 23
    for tag in tags:
        width = len(tag) * 6.9 + 18
        body += f'<rect x="{x}" y="161" width="{width}" height="25" rx="12.5" fill="{t["bg"]}" stroke="{t["border"]}"/>'
        body += f'<text x="{x+9}" y="177" class="muted" font-size="11.2">{escape(tag)}</text>'
        x += width + 7
    body += f'<path d="M390 175h18m-6-6 6 6-6 6" fill="none" stroke="{t["blue"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
    return svg(440, 208, f'{name} — {" ".join(lines)}', body, theme)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        (OUT / f'hero-{theme}.svg').write_text(hero(theme))
        for project in PROJECTS:
            (OUT / f'{project[0]}-{theme}.svg').write_text(card(project, theme))
    print(f'Built {len(THEMES) * (len(PROJECTS) + 1)} profile SVG assets.')


if __name__ == '__main__':
    main()
