# Sakura Nocturne

Ein dunkles Theme für IntelliJ, Rider, Godot und Godot Mono. Kitty und Neovim liegen in den bestehenden Dotfiles-Ordnern dieses Repositories. Die Hauptschriftfarbe ist `#EDA3B1`, der Editorhintergrund `#17171B`; weitere Farben sind Pink, Magenta und Rot auf dunkelgrauen bis schwarzen Flächen.

## IntelliJ und Rider

`jetbrains/Sakura-Nocturne-IntelliJ.jar` enthält das Oberflächen- und Editor-Theme für beide IDEs. In **Settings → Plugins → Install Plugin from Disk** die JAR auswählen und nach dem Neustart **Sakura Nocturne** als Theme wählen. `jetbrains/Sakura Nocturne.icls` ist das separat importierbare Editor-Farbschema. `jetbrains/rider-2026.2/` enthält zusätzlich die aktivierten Rider-Einstellungen und das dort angepasste Farbschema. Die JSON-Datei, die Vorschau und `build_sakura.py` sind Quellen für Anpassungen; das Skript erzeugt JAR, JSON und `.icls` erneut.

## Godot und Godot Mono 4.6

`godot/Sakura-Nocturne.tet` ist das Skripteditor-Theme. Auf macOS nach `~/Library/Application Support/Godot/text_editor_themes/` kopieren und unter **Editor → Editor Settings → Text Editor → Theme → Color Theme** `Sakura-Nocturne` wählen.

`godot/Sakura-Nocturne-Editor.tres` ergänzt die Farben der Editoroberfläche. Nach `~/Library/Application Support/Godot/editor_themes/` kopieren und unter **Interface → Theme** als `Custom Theme` wählen. Dort `Color Preset: Custom`, `Base Color: #1D1D22`, `Accent Color: #D977A9`, `Contrast: 0.18` und `Use System Accent Color: Off` einstellen. Godot und Godot Mono derselben Version nutzen auf macOS dieselben Editor-Einstellungen.

Die Werte für visuelle Shader stehen in `godot/sakura-settings.json`. Die Datei enthält nur Theme-Einstellungen und keine persönlichen Editor- oder Projektpfade. Auf macOS können bei geschlossenem Godot alle Einstellungen mit `python3 godot/install_macos.py` übernommen werden; das Skript legt vorher eine Sicherung der vorhandenen Editor-Einstellungen an. `godot/build/` enthält die Erzeugungs- und Prüfskripte.

Die ursprünglichen ZIP-Pakete liegen unter `releases/`; die bearbeitbaren Einzeldateien liegen in den jeweiligen Konfigurationsordnern.
