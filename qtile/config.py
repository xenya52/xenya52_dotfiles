##############################
######imports#################
##############################
import os
import re
import socket
import subprocess

from libqtile import bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from Core.Layouts import layouts

import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])

#---------------#
#   SETTINGS    #
#---------------#

mod = "mod4"
terminal = "kitty"
browser = "firefox"
notes = "obsidian"
devEnviroment = "intellij-idea-ultimate"
rofi = "rofi -show drun"

#terminal = guess_terminal()


#---------------#
#  KEYBINDINGS  #
#---------------#
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    ############## Own config
    Key([mod], "F5", lazy.spawn("pactl -- set-sink-volume 0 -5%")),
    Key([mod], "F6", lazy.spawn("pactl -- set-sink-volume 0 +5%")),
    Key([mod], "F8", lazy.spawn("xbacklight -dec 5")),
    Key([mod], "F9", lazy.spawn("xbacklight -inc 5")),
    Key([mod], "f", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "o", lazy.spawn(notes), desc="Launch obsidian"),
    Key([mod], "i", lazy.spawn(devEnviroment), desc="Launch intellij"),
    Key([mod], "s", lazy.spawn(rofi), desc="Launch rofi"),
    #############
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod, "control"], "q", lazy.spawn(lock), desc ="Locking you screen"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

#---------------#
#   WORKSPACES  #
#---------------#

groups = []

group_names = ["1", "2", "3", "4","5"]
group_labels = ["[󰣇 ]", "[ ]", "[ ] ", "[󱓧 ]","[󰿎 ]"]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall","monadtall","monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#---------------------------#
#        LAYOUTS            #
#---------------------------#

#layouts = [
#        layout.Max(
#                   margin=20,
#                   border_normal="EDA3B1",
#                   border_focus="8C367C",
#                   border_width=2,
#                   ),
#        layout.Columns(
#                       margin=20, 
#                       border_normal="EDA3B1", 
#                       border_focus="8C367C",
#                       border_width=2,
#                       ),
#]

#-----#
# BAR #
#-----#

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=15,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        
        wallpaper = "~/.config/qtile/Images/wallpaper.jpg",
        wallpaper_mode = "stretch",

        top=bar.Bar(
            [
                widget.Sep(
                    background="#33132D",
                    linewidth=0,
                    padding=6,
                ),
                widget.Clock(
                    background = "#33132D",
                    foreground = "#EDA3B1",
                    format = " %d/%m/%Y",
                    update_interval = 60.0,
                ),
                widget.Clock(
                    background = "#42193B",
                    foreground = "#EDA3B1",
                    format = " %H:%M",
                    update_interval = 60.0,
                ),

                widget.Systray(
                ),
                widget.Prompt(
                ),
                widget.Spacer(
                ),
                widget.TextBox(
                    text = '',
                    foreground = "#EDA3B1",
                    padding = 0,
                    fontsize = 42,
                ),
                widget.Image(
                    background="#EDA3B1",
                    filename="~/.config/qtile/Images/lucyProfilePicTransparent.png",
                    scale="true"
                ),
                widget.GroupBox(
                    background = "#EDA3B1",
                    inactive = "#521F49",
                    active = "#8C367C",
                    rounded=True,
                    highlight_color="#702B6333",
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    foreground="#EDA3B1",
                    padding=0,
                    fontsize=42,
                ),
                widget.Spacer(
                ),
                widget.TextBox(
                    text='',
                    foreground="#8C367C",
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background="#8C367C",
                    foreground="#EDA3B1",
                    format="󰘚 {load_percent}%"
                ),
                widget.TextBox(
                    text='',
                    foreground="#702B63",
                    background="#8C367C",
                    padding=0,
                    fontsize=42,
                ),
                widget.Memory(
                    format=" {MemUsed: .0f}{mm}",
                    background="#702B63",
                    foreground="#EDA3B1",
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#702B63",
                    foreground="#612556",
                    padding=0,
                    fontsize=42
                ),
                widget.Battery(
                    format="󰁺{char} {percent:1.0%} ",
                    charge_char="↑",
                    discharge_char="↓",
                    full_char="!",
                    low_foreground="#FF-0001",
                    background="#612555",
                    foreground="#EDA2B1",
                ),
                widget.TextBox(
                    text='',
                    background="#612556",
                    foreground="#521F49",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=" ",
                    foreground = "#EDA3B1",
                    background = "#521F49",
                ),
                widget.KeyboardLayout(
                    background="#521F49",
                    foreground="#EDA3B1",
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background="#521F49",
                    foreground="#42193B",
                    padding=0,
                    fontsize=42,
                ),
                widget.Backlight(
                    backlight_name = "intel_backlight",
                    format="󰍹 {percent:2.0%} ",
                    background = "#42193B",
                    foreground = "#EDA3B1",
                    scroll = True,
                ),
                widget.TextBox(
                    text='',
                    background = "#42193B",
                    foreground = "#33132D",
                    padding=0,
                    fontsize=42
                ),
                widget.Volume(
                    background ="#33132D",
                    foreground ="#EDA3B1",
                    fmt=" {} "
                ),
                widget.Sep(
                    background = "#33132D",
                    linewidth=0,
                    padding=6,
                ),
            ],
            24,
            margin = [5, 5, 0, 5],
            background = "#32323000",
            background_opacity = 0.5,
        ),
    ),
]

#-----------------------#
#   FLOATING WINDOWS    #
#-----------------------#

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus="#9ccfd8",
    border_normal="#31748f"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
