import os
import re
import socket
import subprocess

from libqtile import bar, widget, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from Core.Layouts import layouts, floating_layout
from Core.Groups import groups
from Core.Keybindings import keys
from Core.Screen import screens, widget_defaults

import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])

#extension_defaults = widget_defaults.copy()

dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
