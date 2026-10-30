"""Install Sakura Nocturne into an existing Godot 4.6 macOS profile."""

import argparse
import json
import os
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def color_value(hex_color: str) -> str:
    channels = [int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    return "Color(" + ", ".join(f"{channel:.8f}" for channel in channels) + ", 1)"


def install(settings_dir: Path) -> None:
    source = Path(__file__).resolve().parent
    palette = json.loads((source / "sakura-settings.json").read_text(encoding="utf-8"))
    settings_file = settings_dir / "editor_settings-4.6.tres"
    if not settings_file.is_file():
        raise FileNotFoundError(f"Godot 4.6 settings not found: {settings_file}")
    original = settings_file.read_text(encoding="utf-8")
    if "[resource]\n" not in original:
        raise ValueError("Godot editor settings have no [resource] section")

    text_theme_dir = settings_dir / "text_editor_themes"
    editor_theme_dir = settings_dir / "editor_themes"
    text_theme_dir.mkdir(parents=True, exist_ok=True)
    editor_theme_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / "Sakura-Nocturne.tet", text_theme_dir / "Sakura-Nocturne.tet")
    custom_theme = editor_theme_dir / "Sakura-Nocturne-Editor.tres"
    shutil.copy2(source / "Sakura-Nocturne-Editor.tres", custom_theme)

    values = {
        "interface/theme/color_preset": '"Custom"',
        "interface/theme/base_color": color_value(palette["interface/theme/base_color"]),
        "interface/theme/accent_color": color_value(palette["interface/theme/accent_color"]),
        "interface/theme/use_system_accent_color": "false",
        "interface/theme/contrast": str(palette["interface/theme/contrast"]),
        "interface/theme/custom_theme": json.dumps(str(custom_theme)),
        "text_editor/theme/color_theme": json.dumps(palette["text_editor/theme/color_theme"]),
    }
    values.update({key: color_value(color) for key, color in palette["visual_editor_colors"].items()})

    updated = original
    for key, value in values.items():
        entry = f"{key} = {value}"
        pattern = re.compile(r"^" + re.escape(key) + r" = .*?$", re.MULTILINE)
        if pattern.search(updated):
            updated = pattern.sub(lambda _: entry, updated, count=1)
        else:
            updated = updated.replace("[resource]\n", "[resource]\n" + entry + "\n", 1)
    updated = re.sub(r"^text_editor/theme/highlighting/background_color = .*\n", "", updated, count=1, flags=re.MULTILINE)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    backup = settings_dir / f"editor_settings-4.6.before-sakura-{timestamp}.tres"
    shutil.copy2(settings_file, backup)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=settings_dir, prefix=".sakura-settings-", delete=False) as handle:
        handle.write(updated)
        temporary = Path(handle.name)
    os.chmod(temporary, settings_file.stat().st_mode)
    os.replace(temporary, settings_file)
    print(f"Installed Sakura Nocturne; backup: {backup}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--settings-dir",
        type=Path,
        default=Path.home() / "Library/Application Support/Godot",
        help="Godot application support directory",
    )
    install(parser.parse_args().settings_dir.expanduser())
