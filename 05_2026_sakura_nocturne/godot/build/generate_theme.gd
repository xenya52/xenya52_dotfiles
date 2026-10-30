extends SceneTree

func _initialize() -> void:
	var theme := Theme.new()
	var fg := Color("#EDA3B1")
	var bright := Color("#F8D3DC")
	var muted := Color("#AD8996")
	var accent := Color("#D977A9")
	var selection := Color("#543245")
	var control_types := ["Label", "Button", "CheckBox", "CheckButton", "MenuButton", "OptionButton", "LinkButton", "PopupMenu", "Tree", "ItemList", "LineEdit", "TextEdit", "TabBar"]
	for control_type in control_types:
		theme.set_color("font_color", control_type, fg)
		theme.set_color("font_hover_color", control_type, bright)
		theme.set_color("font_pressed_color", control_type, bright)
		theme.set_color("font_disabled_color", control_type, muted)
		theme.set_color("font_selected_color", control_type, bright)
		theme.set_color("font_unselected_color", control_type, muted)
	for control_type in ["LineEdit", "TextEdit"]:
		theme.set_color("selection_color", control_type, selection)
		theme.set_color("caret_color", control_type, bright)
		theme.set_color("font_placeholder_color", control_type, muted)
	theme.set_color("default_color", "RichTextLabel", fg)
	theme.set_color("font_color", "CodeEdit", fg)
	theme.set_color("font_color", "Editor", fg)
	theme.set_color("accent_color", "Editor", accent)
	var output := ProjectSettings.globalize_path("res://").path_join("../Sakura-Nocturne-Editor.tres").simplify_path()
	var result := ResourceSaver.save(theme, output)
	if result != OK:
		printerr("Could not save custom editor theme: ", result)
		quit(1)
		return
	var loaded := load(output) as Theme
	if loaded == null or loaded.get_color("font_color", "Label") != fg:
		printerr("Theme validation failed")
		quit(1)
		return
	print("Theme validated: ", output, " Label font=", loaded.get_color("font_color", "Label").to_html(false))
	quit()
