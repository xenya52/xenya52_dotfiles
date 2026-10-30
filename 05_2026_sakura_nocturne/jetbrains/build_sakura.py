import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUT = ROOT
OUT.mkdir(exist_ok=True)

P = {
    'black': '#0E0E11',
    'editor': '#17171B',
    'panel': '#1D1D22',
    'raised': '#26262C',
    'border': '#39343C',
    'text': '#EDA3B1',
    'textBright': '#F8D3DC',
    'muted': '#AD8996',
    'selection': '#543245',
    'selectionInactive': '#393039',
    'accent': '#D977A9',
    'pink': '#F1A1CF',
    'magenta': '#D78BDF',
    'rose': '#F2B7A9',
    'red': '#E77B87',
}

theme = {
    'name': 'Sakura Nocturne',
    'dark': True,
    'author': 'Custom theme',
    'editorScheme': '/Sakura Nocturne.xml',
    'colors': P,
    'ui': {
        '*': {
            'background': 'panel',
            'foreground': 'text',
            'selectionBackground': 'selection',
            'selectionForeground': 'textBright',
            'selectionInactiveBackground': 'selectionInactive',
            'selectionBackgroundInactive': 'selectionInactive',
        },
        'Panel.background': 'panel',
        'Viewport.background': 'panel',
        'ScrollPane.background': 'panel',
        'Tree.background': 'panel',
        'Tree.foreground': 'text',
        'List.background': 'panel',
        'List.foreground': 'text',
        'Table.background': 'panel',
        'Table.foreground': 'text',
        'TextField.background': 'raised',
        'TextField.foreground': 'text',
        'TextArea.background': 'editor',
        'TextArea.foreground': 'text',
        'PasswordField.background': 'raised',
        'PasswordField.foreground': 'text',
        'ComboBox.background': 'raised',
        'ComboBox.foreground': 'text',
        'Button.background': 'raised',
        'Button.foreground': 'textBright',
        'Label.foreground': 'text',
        'Separator.foreground': 'border',
        'Component.focusColor': 'accent',
        'Component.borderColor': 'border',
        'ProgressBar.foreground': 'accent',
        'ProgressBar.background': 'raised',
        'ToolWindow.background': 'panel',
        'ToolWindow.Button.selectedBackground': 'selection',
        'ToolWindow.Button.selectedForeground': 'textBright',
        'EditorTabs.background': 'panel',
        'EditorTabs.selectedForeground': 'textBright',
        'EditorTabs.selectedBackground': 'editor',
        'EditorTabs.underlineColor': 'accent',
        'EditorTabs.underlinedTabBackground': 'editor',
        'EditorTabs.inactiveColoredFileBackground': 'panel',
        'DefaultTabs.background': 'panel',
        'DefaultTabs.underlineColor': 'accent',
        'TabbedPane.background': 'panel',
        'TabbedPane.foreground': 'text',
        'Menu.background': 'panel',
        'Menu.foreground': 'text',
        'MenuItem.background': 'panel',
        'MenuItem.foreground': 'text',
        'PopupMenu.background': 'panel',
        'PopupMenu.foreground': 'text',
        'PopupMenu.borderColor': 'border',
        'SearchEverywhere.SearchField.background': 'raised',
        'SearchEverywhere.SearchField.foreground': 'textBright',
        'SearchEverywhere.List.background': 'panel',
        'StatusBar.background': 'black',
        'StatusBar.foreground': 'muted',
        'Notification.background': 'raised',
        'Notification.foreground': 'text',
        'Link.activeForeground': 'pink',
        'Link.hoverForeground': 'textBright',
        'Link.visitedForeground': 'magenta',
    },
    'icons': {
        'ColorPalette': {
            'Actions.Blue': P['pink'],
            'Actions.Red': P['red'],
            'Actions.Yellow': P['rose'],
            'Actions.Green': P['accent'],
            'Actions.Grey': P['muted'],
            'Objects.Blue': P['pink'],
            'Objects.Red': P['red'],
            'Objects.Purple': P['magenta'],
            'Objects.Pink': P['text'],
            'Objects.Grey': P['muted'],
        }
    }
}

scheme = ET.Element('scheme', {'name': 'Sakura Nocturne', 'version': '142', 'parent_scheme': 'Darcula'})
colors = ET.SubElement(scheme, 'colors')
color_entries = {
    'CARET_COLOR': 'textBright',
    'CARET_ROW_COLOR': 'panel',
    'GUTTER_BACKGROUND': 'black',
    'LINE_NUMBERS_COLOR': 'muted',
    'LINE_NUMBER_ON_CARET_ROW_COLOR': 'textBright',
    'SELECTION_BACKGROUND': 'selection',
    'SELECTION_FOREGROUND': 'textBright',
    'RIGHT_MARGIN_COLOR': 'border',
    'INDENT_GUIDE': 'border',
    'SELECTED_INDENT_GUIDE': 'accent',
    'WHITESPACES': 'muted',
    'CONSOLE_BACKGROUND_KEY': 'editor',
}
for key, alias in color_entries.items():
    ET.SubElement(colors, 'option', {'name': key, 'value': P[alias][1:].lower()})

attrs = ET.SubElement(scheme, 'attributes')
attribute_entries = {
    'TEXT': {'FOREGROUND': 'text', 'BACKGROUND': 'editor'},
    'DEFAULT_IDENTIFIER': {'FOREGROUND': 'text'},
    'DEFAULT_KEYWORD': {'FOREGROUND': 'pink', 'FONT_TYPE': '1'},
    'DEFAULT_STRING': {'FOREGROUND': 'rose'},
    'DEFAULT_NUMBER': {'FOREGROUND': 'magenta'},
    'DEFAULT_CONSTANT': {'FOREGROUND': 'magenta'},
    'DEFAULT_LINE_COMMENT': {'FOREGROUND': 'muted'},
    'DEFAULT_BLOCK_COMMENT': {'FOREGROUND': 'muted'},
    'DEFAULT_DOC_COMMENT': {'FOREGROUND': 'muted'},
    'DEFAULT_DOC_COMMENT_TAG': {'FOREGROUND': 'pink'},
    'DEFAULT_CLASS_NAME': {'FOREGROUND': 'textBright'},
    'DEFAULT_INTERFACE_NAME': {'FOREGROUND': 'textBright'},
    'DEFAULT_FUNCTION_DECLARATION': {'FOREGROUND': 'pink'},
    'DEFAULT_FUNCTION_CALL': {'FOREGROUND': 'textBright'},
    'DEFAULT_INSTANCE_METHOD': {'FOREGROUND': 'textBright'},
    'DEFAULT_STATIC_METHOD': {'FOREGROUND': 'pink'},
    'DEFAULT_INSTANCE_FIELD': {'FOREGROUND': 'text'},
    'DEFAULT_STATIC_FIELD': {'FOREGROUND': 'magenta'},
    'DEFAULT_PARAMETER': {'FOREGROUND': 'text'},
    'DEFAULT_LOCAL_VARIABLE': {'FOREGROUND': 'text'},
    'DEFAULT_GLOBAL_VARIABLE': {'FOREGROUND': 'text'},
    'DEFAULT_METADATA': {'FOREGROUND': 'pink'},
    'DEFAULT_TAG': {'FOREGROUND': 'pink'},
    'DEFAULT_ATTRIBUTE': {'FOREGROUND': 'textBright'},
    'DEFAULT_ENTITY': {'FOREGROUND': 'magenta'},
    'DEFAULT_VALID_STRING_ESCAPE': {'FOREGROUND': 'pink'},
    'DEFAULT_INVALID_STRING_ESCAPE': {'FOREGROUND': 'red'},
    'DEFAULT_OPERATION_SIGN': {'FOREGROUND': 'text'},
    'DEFAULT_BRACES': {'FOREGROUND': 'text'},
    'DEFAULT_BRACKETS': {'FOREGROUND': 'text'},
    'DEFAULT_COMMA': {'FOREGROUND': 'text'},
    'DEFAULT_DOT': {'FOREGROUND': 'text'},
    'DEFAULT_SEMICOLON': {'FOREGROUND': 'text'},
    'ERRORS_ATTRIBUTES': {'EFFECT_COLOR': 'red', 'EFFECT_TYPE': '2'},
    'WARNING_ATTRIBUTES': {'EFFECT_COLOR': 'rose', 'EFFECT_TYPE': '2'},
    'TODO_DEFAULT_ATTRIBUTES': {'FOREGROUND': 'pink', 'FONT_TYPE': '1'},
    'FOLDED_TEXT_ATTRIBUTES': {'FOREGROUND': 'muted', 'BACKGROUND': 'raised'},
    'MATCHED_BRACE_ATTRIBUTES': {'FOREGROUND': 'textBright', 'BACKGROUND': 'selection'},
    'SEARCH_RESULT_ATTRIBUTES': {'FOREGROUND': 'textBright', 'BACKGROUND': 'selection'},
}
for key, entries in attribute_entries.items():
    opt = ET.SubElement(attrs, 'option', {'name': key})
    val = ET.SubElement(opt, 'value')
    for property_name, alias in entries.items():
        value = P[alias][1:].lower() if alias in P else alias
        ET.SubElement(val, 'option', {'name': property_name, 'value': value})

ET.indent(scheme, space='  ')
scheme_bytes = ET.tostring(scheme, encoding='utf-8', xml_declaration=True)
plugin_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<idea-plugin>
  <id>com.custom.sakura.nocturne.theme</id>
  <name>Sakura Nocturne</name>
  <version>1.0.0</version>
  <description><![CDATA[Ein dunkles Sakura-Theme mit rosafarbenem Text, Pink und Magenta.]]></description>
  <depends>com.intellij.modules.platform</depends>
  <extensions defaultExtensionNs="com.intellij">
    <themeProvider id="8b40a288-df63-4f6c-b74b-43b042e8958b" path="/sakura-nocturne.theme.json"/>
  </extensions>
</idea-plugin>
'''.encode('utf-8')

theme_bytes = (json.dumps(theme, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
(OUT / 'Sakura Nocturne.icls').write_bytes(scheme_bytes)
(OUT / 'sakura-nocturne.theme.json').write_bytes(theme_bytes)
jar = OUT / 'Sakura-Nocturne-IntelliJ.jar'
with zipfile.ZipFile(jar, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    z.writestr('META-INF/MANIFEST.MF', 'Manifest-Version: 1.0\r\n\r\n')
    z.writestr('META-INF/plugin.xml', plugin_xml)
    z.writestr('sakura-nocturne.theme.json', theme_bytes)
    z.writestr('Sakura Nocturne.xml', scheme_bytes)

# Basic format and package checks.
assert json.loads(theme_bytes)['editorScheme'] == '/Sakura Nocturne.xml'
assert ET.fromstring(scheme_bytes).attrib['name'] == 'Sakura Nocturne'
assert ET.fromstring(plugin_xml).find('.//themeProvider').attrib['path'] == '/sakura-nocturne.theme.json'
with zipfile.ZipFile(jar) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == {'META-INF/MANIFEST.MF', 'META-INF/plugin.xml', 'sakura-nocturne.theme.json', 'Sakura Nocturne.xml'}
assert P['text'] == '#EDA3B1'
for item in P.values():
    assert re.fullmatch(r'#[0-9A-Fa-f]{6}', item)
print('OK', jar, jar.stat().st_size, 'bytes')
