#!/usr/bin/env python3

from __future__ import annotations

import math
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/home/knox/workspace/github_work")
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


REPOS = {
    "ToolmeshAI": {
        "tagline": "Practical public repos around MCP, agent workflows, docs-to-context tooling, and browser automation.",
        "eyebrow": "Portfolio Hub",
        "accent": "#C8553D",
        "accent_soft": "#F2C3A7",
        "shape": "portfolio",
        "command": None,
    },
    "mcp-saas-foundry": {
        "tagline": "Forkable SaaS MCP starter with blueprint docs, template code, and ship-ready guardrails.",
        "eyebrow": "Flagship Blueprint",
        "accent": "#EF8354",
        "accent_soft": "#F7C59F",
        "shape": "grid",
        "command": ["npm", "run", "blueprint", "--", "--section", "docs"],
    },
    "safe-mcp-config": {
        "tagline": "Zero-dependency CLI for catching risky MCP config patterns before they leak into public repos.",
        "eyebrow": "Security Utility",
        "accent": "#4CB944",
        "accent_soft": "#B4E197",
        "shape": "scan",
        "command": ["node", "src/cli.mjs", "--format", "json", "--fail-on", "none", "examples/unsafe-mcp.json"],
    },
    "docs-to-context": {
        "tagline": "Bundle scattered docs into one clean Markdown context file for LLMs and coding agents.",
        "eyebrow": "Docs Pipeline",
        "accent": "#2E86AB",
        "accent_soft": "#A7D6E8",
        "shape": "pages",
        "command": ["node", "src/cli.mjs", "samples/docs"],
    },
    "awesome-mcp-workflows": {
        "tagline": "Bilingual catalog of MCP workflow patterns, server shapes, and launchable combinations with evidence labels.",
        "eyebrow": "Curated Catalog",
        "accent": "#7A5CFA",
        "accent_soft": "#CEC4FF",
        "shape": "workflow",
        "command": None,
    },
    "browser-agent-recipes": {
        "tagline": "Browser-native agent recipes with clear inputs, outputs, guardrails, and demo-ready operational value.",
        "eyebrow": "Recipe Library",
        "accent": "#E56B6F",
        "accent_soft": "#F4C2C2",
        "shape": "recipe",
        "command": None,
    },
    "mcp-smoke-test": {
        "tagline": "Zero-dependency CLI for proving a stdio MCP server can initialize and answer a real follow-up probe.",
        "eyebrow": "Protocol Utility",
        "accent": "#1F8A70",
        "accent_soft": "#A7E3D6",
        "shape": "scan",
        "command": ["node", "bin/mcp-smoke-test.js", "--config", "examples/mcp.config.json", "--server", "fake-fixture", "--format", "text"],
    },
    "llms-txt-check": {
        "tagline": "Zero-dependency CLI for validating llms.txt structure before broken links or weak summaries reach production repos.",
        "eyebrow": "Context Utility",
        "accent": "#3C6E71",
        "accent_soft": "#BFD7D9",
        "shape": "pages",
        "command": ["node", "bin/llms-txt-check.js", "--file", "examples/good/llms.txt", "--format", "text"],
    },
    "mcp-http-smoke": {
        "tagline": "Minimal HTTP MCP smoke tester that proves initialize, initialized, and one real capability probe over JSON-RPC.",
        "eyebrow": "HTTP Utility",
        "accent": "#0E9594",
        "accent_soft": "#9AD1D4",
        "shape": "scan",
        "command": ["node", "scripts/demo.js"],
    },
    "browser-agent-starter": {
        "tagline": "Minimal browser-ready starter with dry-run planning, shared config, and structured artifacts for browser-agent workflows.",
        "eyebrow": "Starter Scaffold",
        "accent": "#C97B63",
        "accent_soft": "#F2C6B4",
        "shape": "workflow",
        "command": ["node", "src/cli.js", "run", "docs-audit", "--config", "examples/docs-audit.json", "--output", "tmp/docs-audit-assets", "--dry-run"],
    },
    "github-agent-action": {
        "tagline": "Small GitHub Action that turns workflow inputs into reusable execution briefs and JSON manifests for later agent runs.",
        "eyebrow": "Workflow Action",
        "accent": "#355070",
        "accent_soft": "#B9C6D3",
        "shape": "workflow",
        "command": ["node", "scripts/demo.js"],
    },
}

PALETTE = {
    "bg": "#F6F3EA",
    "ink": "#132238",
    "muted": "#5D6A78",
    "line": "#D7D1C2",
    "panel": "#FFFDFC",
    "terminal_bg": "#0F1726",
    "terminal_top": "#1B2537",
    "terminal_text": "#E8EDF7",
    "terminal_muted": "#9AA7BD",
    "terminal_cmd": "#80ED99",
    "signal": "#E94F37",
}


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def command_output(repo_path: Path, command: list[str]) -> str:
    result = subprocess.run(
        command,
        cwd=repo_path,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return result.stdout.strip()


def draw_wrapped(draw: ImageDraw.ImageDraw, text: str, box: tuple[int, int, int, int], font, fill, spacing=8) -> int:
    x0, y0, x1, _ = box
    words = text.split()
    lines: list[str] = []
    current = []
    for word in words:
        trial = " ".join(current + [word])
        width = draw.textbbox((0, 0), trial, font=font)[2]
        if current and width > (x1 - x0):
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))

    y = y0
    for line in lines:
        draw.text((x0, y), line, font=font, fill=fill)
        y += font.size + spacing
    return y


def draw_shape(draw: ImageDraw.ImageDraw, repo: str, accent: str, accent_soft: str) -> None:
    if REPOS[repo]["shape"] == "grid":
        for row in range(4):
            for col in range(6):
                x = 760 + col * 70
                y = 140 + row * 70
                fill = accent if (row + col) % 3 == 0 else accent_soft
                draw.rounded_rectangle((x, y, x + 42, y + 42), radius=12, fill=fill)
                draw.rounded_rectangle((x + 18, y + 18, x + 56, y + 56), radius=12, outline=PALETTE["ink"], width=3)
    elif REPOS[repo]["shape"] == "scan":
        draw.rounded_rectangle((800, 120, 1140, 520), radius=28, outline=accent, width=8, fill="#FFFFFF")
        for y in range(180, 460, 56):
            draw.line((850, y, 1080, y), fill=PALETTE["line"], width=4)
            draw.ellipse((1096, y - 12, 1120, y + 12), fill=accent if y < 300 else accent_soft)
        draw.arc((730, 80, 1110, 460), start=300, end=80, fill=accent, width=10)
        draw.arc((700, 50, 1140, 490), start=110, end=230, fill=accent_soft, width=10)
    elif REPOS[repo]["shape"] == "pages":
        offsets = [(0, 0), (28, 24), (56, 48)]
        for index, (ox, oy) in enumerate(offsets):
            draw.rounded_rectangle(
                (770 + ox, 120 + oy, 1110 + ox, 500 + oy),
                radius=26,
                fill="#FFFFFF",
                outline=accent if index == 2 else PALETTE["line"],
                width=6 if index == 2 else 3,
            )
            for line_y in range(180 + oy, 440 + oy, 50):
                line_w = 230 if line_y % 100 else 180
                draw.line((830 + ox, line_y, 830 + ox + line_w, line_y), fill=accent_soft, width=10)
        draw.line((760, 520, 1160, 520), fill=accent, width=12)
    elif REPOS[repo]["shape"] == "portfolio":
        cards = [
            ("mcp", 790, 120, accent),
            ("safe", 980, 150, accent_soft),
            ("docs", 870, 290, "#E7D7C1"),
            ("flows", 1060, 320, accent),
            ("browser", 740, 410, accent_soft),
        ]
        for label, x, y, fill in cards:
            draw.rounded_rectangle((x, y, x + 180, y + 110), radius=20, fill=fill, outline=PALETTE["ink"], width=3)
            draw.text((x + 18, y + 34), label, font=load_font(FONT_SANS_BOLD, 26), fill=PALETTE["ink"])
    elif REPOS[repo]["shape"] == "workflow":
        nodes = [
            ("server", 790, 150, accent),
            ("workflow", 1000, 150, accent_soft),
            ("recipe", 895, 310, "#E7D7C1"),
        ]
        for label, x, y, fill in nodes:
            draw.rounded_rectangle((x, y, x + 210, y + 90), radius=24, fill=fill, outline=PALETTE["ink"], width=3)
            draw.text((x + 24, y + 28), label, font=load_font(FONT_SANS_BOLD, 28), fill=PALETTE["ink"])
        draw.line((915, 240, 955, 310), fill=accent, width=8)
        draw.line((1105, 240, 1045, 310), fill=accent, width=8)
    elif REPOS[repo]["shape"] == "recipe":
        cards = [
            ("qa", 770, 140, accent_soft),
            ("ops", 980, 140, "#E7D7C1"),
            ("support", 875, 300, accent),
            ("finance", 1085, 300, accent_soft),
        ]
        for label, x, y, fill in cards:
            draw.rounded_rectangle((x, y, x + 170, y + 96), radius=22, fill=fill, outline=PALETTE["ink"], width=3)
            draw.text((x + 22, y + 30), label, font=load_font(FONT_SANS_BOLD, 26), fill=PALETTE["ink"])


def make_social_card(repo: str, target: Path) -> None:
    ensure_dir(target.parent)
    image = Image.new("RGB", (1280, 640), PALETTE["bg"])
    draw = ImageDraw.Draw(image)

    title_font = load_font(FONT_SANS_BOLD, 68)
    eyebrow_font = load_font(FONT_SANS_BOLD, 24)
    body_font = load_font(FONT_SANS, 30)
    chip_font = load_font(FONT_SANS_BOLD, 22)
    mono_font = load_font(FONT_MONO, 22)

    accent = REPOS[repo]["accent"]
    accent_soft = REPOS[repo]["accent_soft"]

    draw.rounded_rectangle((70, 60, 1210, 580), radius=38, outline=PALETTE["line"], width=3, fill=PALETTE["panel"])
    draw.rounded_rectangle((90, 86, 350, 126), radius=18, fill=accent)
    draw.text((112, 95), REPOS[repo]["eyebrow"], font=eyebrow_font, fill="#FFFFFF")

    draw.text((95, 160), repo, font=title_font, fill=PALETTE["ink"])
    tagline_bottom = draw_wrapped(
        draw,
        REPOS[repo]["tagline"],
        (95, 258, 670, 450),
        body_font,
        PALETTE["muted"],
        spacing=12,
    )

    chips = ["ToolmeshAI", "Open Source", "Bilingual Docs"]
    chip_x = 95
    for chip in chips:
        width = draw.textbbox((0, 0), chip, font=chip_font)[2] + 36
        draw.rounded_rectangle((chip_x, tagline_bottom + 26, chip_x + width, tagline_bottom + 66), radius=18, outline=accent, width=2)
        draw.text((chip_x + 18, tagline_bottom + 36), chip, font=chip_font, fill=accent)
        chip_x += width + 14

    draw_shape(draw, repo, accent, accent_soft)

    draw.text((95, 520), "github.com/ToolmeshAI", font=mono_font, fill=PALETTE["muted"])
    draw.text((1000, 520), "STAR-WORTHY", font=chip_font, fill=accent)

    image.save(target)


def terminal_frame(title: str, command: str, lines: list[str], progress: float) -> Image.Image:
    image = Image.new("RGB", (1440, 900), PALETTE["terminal_bg"])
    draw = ImageDraw.Draw(image)
    title_font = load_font(FONT_SANS_BOLD, 28)
    mono_font = load_font(FONT_MONO, 24)
    mono_small = load_font(FONT_MONO, 20)

    draw.rounded_rectangle((60, 50, 1380, 850), radius=28, fill=PALETTE["terminal_bg"], outline="#21304A", width=3)
    draw.rounded_rectangle((60, 50, 1380, 112), radius=28, fill=PALETTE["terminal_top"])
    draw.rectangle((60, 84, 1380, 112), fill=PALETTE["terminal_top"])
    for index, color in enumerate(("#FF5F56", "#FFBD2E", "#27C93F")):
        draw.ellipse((88 + index * 28, 72, 108 + index * 28, 92), fill=color)
    draw.text((160, 68), title, font=title_font, fill="#F7FAFC")

    draw.text((96, 150), "$ " + command, font=mono_font, fill=PALETTE["terminal_cmd"])

    visible = max(1, math.ceil(len(lines) * progress))
    y = 208
    for line in lines[:visible]:
        fill = PALETTE["terminal_text"]
        if line.startswith(("ℹ", "✔")):
            fill = "#A5F3FC"
        elif "warning" in line.lower() or "risk" in line.lower() or "secret" in line.lower():
            fill = "#FDE68A"
        elif line.startswith("Error"):
            fill = "#FCA5A5"
        wrapped = textwrap.wrap(line, width=100) or [""]
        for subline in wrapped:
            draw.text((96, y), subline, font=mono_small, fill=fill)
            y += 28
        if y > 780:
            break

    return image


def make_demo_assets(repo: str, target_dir: Path) -> None:
    ensure_dir(target_dir)
    output = command_output(ROOT / repo, REPOS[repo]["command"])
    lines = output.splitlines()[:22]
    command = " ".join(REPOS[repo]["command"])

    screenshot = terminal_frame(f"{repo} demo", command, lines, progress=1.0)
    screenshot.save(target_dir / "demo-terminal.png")

    frames = []
    for progress in (0.16, 0.34, 0.52, 0.7, 0.88, 1.0):
        frames.append(terminal_frame(f"{repo} demo", command, lines, progress=progress))
    frames[0].save(
        target_dir / "demo.gif",
        save_all=True,
        append_images=frames[1:],
        duration=[350, 350, 350, 350, 350, 900],
        loop=0,
    )


def main() -> None:
    for repo in REPOS:
        asset_dir = ROOT / repo / "docs" / "assets"
        make_social_card(repo, asset_dir / "social-preview.png")
        if REPOS[repo]["command"]:
            make_demo_assets(repo, asset_dir)
        print(f"generated {repo} assets -> {asset_dir}")


if __name__ == "__main__":
    main()
