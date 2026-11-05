#!/usr/bin/env python3
"""Build the Sakura Nocturne Codex desktop share string and CLI theme."""

import json
import plistlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
COLORS = {
    "background": "#17171B",
    "black": "#0E0E11",
    "panel": "#1D1D22",
    "raised": "#26262C",
    "border": "#39343C",
    "foreground": "#EDA3B1",
    "bright": "#F8D3DC",
    "muted": "#AD8996",
    "selection": "#543245",
    "accent": "#D977A9",
    "pink": "#F1A1CF",
    "magenta": "#D78BDF",
    "rose": "#F2B7A9",
    "red": "#E77B87",
}


def rule(scope, foreground, style=None):
    settings = {"foreground": foreground}
    if style:
        settings["fontStyle"] = style
    return {"scope": scope, "settings": settings}


desktop = {
    "codeThemeId": "rose-pine",
    "theme": {
        "accent": COLORS["accent"],
        "accentSource": "custom",
        "contrast": 60,
        "fonts": {"code": None, "ui": '"Terminus (TTF)"'},
        "ink": COLORS["foreground"],
        "opaqueWindows": True,
        "semanticColors": {
            "diffAdded": COLORS["magenta"],
            "diffRemoved": COLORS["red"],
            "skill": COLORS["pink"],
        },
        "surface": COLORS["background"],
    },
    "variant": "dark",
}

theme = {
    "name": "Sakura Nocturne",
    "author": "lucyhuhn",
    "settings": [
        {
            "settings": {
                "background": COLORS["background"],
                "foreground": COLORS["foreground"],
                "caret": COLORS["pink"],
                "selection": COLORS["selection"],
                "lineHighlight": COLORS["panel"],
                "invisibles": COLORS["border"],
            }
        },
        rule("comment, punctuation.definition.comment", COLORS["muted"], "italic"),
        rule("string, string.quoted, string.template", COLORS["rose"]),
        rule("constant.numeric, constant.language", COLORS["pink"]),
        rule("keyword, storage, storage.type", COLORS["magenta"]),
        rule("keyword.operator, punctuation.accessor", COLORS["accent"]),
        rule("entity.name.function, support.function", COLORS["pink"]),
        rule("entity.name.type, entity.name.class, support.class", COLORS["bright"]),
        rule("variable, variable.other", COLORS["foreground"]),
        rule("variable.parameter", COLORS["rose"]),
        rule("entity.name.tag, support.type.property-name", COLORS["accent"]),
        rule("entity.other.attribute-name", COLORS["pink"]),
        rule("invalid, invalid.illegal", COLORS["red"]),
        rule("markup.heading", COLORS["pink"], "bold"),
        rule("markup.bold", COLORS["bright"], "bold"),
        rule("markup.italic", COLORS["rose"], "italic"),
        rule("markup.underline.link, string.other.link", COLORS["magenta"], "underline"),
        rule("markup.inserted, diff.inserted", COLORS["magenta"]),
        rule("markup.deleted, diff.deleted", COLORS["red"]),
        rule("markup.changed, diff.changed", COLORS["pink"]),
    ],
}

HERE.mkdir(parents=True, exist_ok=True)
(HERE / "Sakura-Nocturne-Codex.theme.txt").write_text(
    "codex-theme-v1:" + json.dumps(desktop, separators=(",", ":")) + "\n",
    encoding="utf-8",
)
(HERE / "sakura-nocturne.tmTheme").write_bytes(plistlib.dumps(theme, fmt=plistlib.FMT_XML))
(HERE / "palette.json").write_text(json.dumps(COLORS, indent=2) + "\n", encoding="utf-8")
