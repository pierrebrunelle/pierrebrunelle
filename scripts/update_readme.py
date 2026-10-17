#!/usr/bin/env python3
"""Sync README.md and hero SVGs with live Pixeltable release stats and Awesome Pixeltable Apps."""

from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / 'README.md'
SVG_PATHS = [ROOT / 'assets' / 'hero-dark.svg', ROOT / 'assets' / 'hero-light.svg']

PIXELTABLE_REPO_API = 'https://api.github.com/repos/pixeltable/pixeltable'
PIXELTABLE_RELEASE_API = 'https://api.github.com/repos/pixeltable/pixeltable/releases/latest'
AWESOME_APPS_README_URL = 'https://raw.githubusercontent.com/pierrebrunelle/awesome-pixeltable-apps/main/README.md'


def fetch_text(url: str) -> str:
    headers = {'User-Agent': 'pierrebrunelle-profile-updater'}
    token = os.environ.get('GITHUB_TOKEN')
    if token and 'api.github.com' in url:
        headers['Authorization'] = f'Bearer {token}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode('utf-8')


def fetch_json(url: str) -> dict:
    return json.loads(fetch_text(url))


def parse_awesome_apps(md: str, limit: int = 5) -> tuple[int, list[dict[str, str]]]:
    count_match = re.search(r'(\d+)\s+apps,\s+newest\s+first', md)
    rows: list[dict[str, str]] = []
    in_table = False
    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith('| App | What it does |'):
            in_table = True
            continue
        if in_table:
            if stripped.startswith('|---'):
                continue
            if not stripped.startswith('|'):
                break
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            if len(cells) >= 4:
                rows.append({
                    'app': cells[0],
                    'description': cells[1],
                    'features': cells[2],
                    'try_it': cells[3],
                })
    total_count = int(count_match.group(1)) if count_match else len(rows)
    return total_count, rows[:limit]


def format_features_chips(features_cell: str) -> str:
    parts = [p.strip() for p in features_cell.split(',') if p.strip()]
    return ' · '.join(f'`{p}`' for p in parts)


def replace_block(content: str, marker: str, replacement: str) -> str:
    pattern = re.compile(
        rf'(<!-- {re.escape(marker)}:START -->).*?(<!-- {re.escape(marker)}:END -->)',
        re.DOTALL,
    )
    return pattern.sub(rf'\1{replacement}\2', content)


def main() -> None:
    repo_data = fetch_json(PIXELTABLE_REPO_API)
    release_data = fetch_json(PIXELTABLE_RELEASE_API)
    awesome_md = fetch_text(AWESOME_APPS_README_URL)

    stars = int(repo_data.get('stargazers_count', 1640))
    forks = int(repo_data.get('forks_count', 228))
    tag_name = release_data.get('tag_name', 'v0.7.18')
    release_url = release_data.get('html_url', f'https://github.com/pixeltable/pixeltable/releases/tag/{tag_name}')
    total_apps, top_apps = parse_awesome_apps(awesome_md, limit=5)

    meta_block = (
        f'\n> 📦 **Latest release:** [`{tag_name}`]({release_url}) '
        f'&nbsp;·&nbsp; ⭐ **{stars:,} stars** '
        f'&nbsp;·&nbsp; 🍴 **{forks:,} forks** '
        f'&nbsp;·&nbsp; 🧪 **[{total_apps} runnable example apps](https://pierrebrunelle.github.io/awesome-pixeltable-apps/)**\n'
    )

    table_lines = [
        f'\n_Auto-synced from [`pierrebrunelle/awesome-pixeltable-apps`](https://github.com/pierrebrunelle/awesome-pixeltable-apps) ({total_apps} apps total, newest first):_',
        '',
        '| App | Architecture & Features | Launch |',
        '| :--- | :--- | :---: |',
    ]
    for item in top_apps:
        app_cell = re.sub(
            r'\[([a-z0-9 ]+)\]',
            lambda m: f'[{m.group(1).title()}]',
            item['app'],
        )
        chips = format_features_chips(item['features'])
        desc = f"{item['description']}<br><sub>{chips}</sub>" if chips else item['description']
        try_badge = item['try_it'].replace('Open in GitHub Codespaces', 'Codespaces')
        table_lines.append(f'| {app_cell} | {desc} | {try_badge} |')

    table_lines.extend([
        '',
        '<div align="right">',
        f'  <sub><a href="https://pierrebrunelle.github.io/awesome-pixeltable-apps/">Browse all {total_apps} runnable apps in the interactive gallery →</a></sub>',
        '</div>\n',
    ])
    apps_block = '\n'.join(table_lines)

    readme = README_PATH.read_text(encoding='utf-8')
    readme = replace_block(readme, 'PIXELTABLE-META', meta_block)
    readme = replace_block(readme, 'AWESOME-APPS', apps_block)
    README_PATH.write_text(readme, encoding='utf-8')

    for svg_path in SVG_PATHS:
        if not svg_path.exists():
            continue
        svg = svg_path.read_text(encoding='utf-8')
        svg = replace_block(
            svg,
            'PXT-VERSION',
            f'<text x="216" y="16" class="mono" font-size="10" fill="#64748b">{tag_name}</text>',
        )
        svg = replace_block(
            svg,
            'PXT-TELEMETRY',
            f'<text x="928" y="304" text-anchor="end">★ {stars:,} STARS · {total_apps} RUNNABLE APPS · APACHE-2.0</text>',
        )
        svg_path.write_text(svg, encoding='utf-8')


if __name__ == '__main__':
    main()
