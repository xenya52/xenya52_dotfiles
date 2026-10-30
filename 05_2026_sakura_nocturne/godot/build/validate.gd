extends SceneTree

func _initialize() -> void:
	var config := ConfigFile.new()
	var theme_dir := ProjectSettings.globalize_path("res://").path_join("..").simplify_path()
	var result := config.load(theme_dir.path_join("Sakura-Nocturne.tet"))
	if result != OK:
		printerr("Cannot read text editor theme: ", result)
		quit(1)
		return
	var fg: String = config.get_value("color_theme", "text_color", "")
	var bg: String = config.get_value("color_theme", "background_color", "")
	var theme := load(theme_dir.path_join("Sakura-Nocturne-Editor.tres")) as Theme
	if fg != "eda3b1ff" or bg != "17171bff" or theme == null or theme.get_color("font_color", "Label") != Color("#EDA3B1"):
		printerr("Theme palette validation failed: ", fg, " / ", bg)
		quit(1)
		return
	print("Theme validated: ", fg, " on ", bg)
	quit()
