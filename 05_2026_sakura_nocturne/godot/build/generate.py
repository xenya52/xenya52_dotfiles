from pathlib import Path

root = Path(__file__).resolve().parent.parent
output = root / "Sakura-Nocturne.tet"

colors = {
    "symbol_color": "EDA3B1",
    "keyword_color": "F1A1CF",
    "control_flow_keyword_color": "D78BDF",
    "base_type_color": "F8D3DC",
    "engine_type_color": "F2B7A9",
    "user_type_color": "F1A1CF",
    "comment_color": "AD8996",
    "doc_comment_color": "AD8996",
    "string_color": "F2B7A9",
    "string_placeholder_color": "D977A9",
    "background_color": "17171B",
    "completion_background_color": "1D1D22",
    "completion_selected_color": "543245",
    "completion_existing_color": "D977A944",
    "completion_scroll_color": "39343C",
    "completion_scroll_hovered_color": "543245",
    "completion_font_color": "EDA3B1",
    "text_color": "EDA3B1",
    "line_number_color": "AD8996",
    "safe_line_number_color": "D977A9",
    "caret_color": "F8D3DC",
    "caret_background_color": "17171B",
    "text_selected_color": "F8D3DC",
    "selection_color": "543245",
    "brace_mismatch_color": "E77B87",
    "current_line_color": "26262C80",
    "line_length_guideline_color": "39343C",
    "word_highlighted_color": "54324588",
    "number_color": "D78BDF",
    "function_color": "F8D3DC",
    "member_variable_color": "EDA3B1",
    "mark_color": "E77B874D",
    "warning_color": "F2B7A933",
    "bookmark_color": "F1A1CF",
    "breakpoint_color": "E77B87",
    "executing_line_color": "D977A9",
    "code_folding_color": "AD8996",
    "folded_code_region_color": "1D1D22",
    "search_result_color": "543245",
    "search_result_border_color": "D977A9",
    "warning_underline_color": "F2B7A9",
    "error_underline_color": "E77B87",
    "gdscript/function_definition_color": "F8D3DC",
    "gdscript/global_function_color": "F1A1CF",
    "gdscript/node_path_color": "F2B7A9",
    "gdscript/node_reference_color": "D977A9",
    "gdscript/annotation_color": "D78BDF",
    "gdscript/string_name_color": "F2B7A9",
    "comment_markers/critical_color": "E77B87",
    "comment_markers/warning_color": "F2B7A9",
    "comment_markers/notice_color": "D977A9",
}

for name, color in colors.items():
    assert len(color) in (6, 8), (name, color)
    int(color, 16)

output.write_text(
    "[color_theme]\n\n"
    + "\n".join(f'{name}="{color.lower() if len(color) == 8 else color.lower() + "ff"}"' for name, color in colors.items())
    + "\n",
    encoding="utf-8",
)
print(output)
