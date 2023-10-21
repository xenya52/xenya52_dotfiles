# ██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗███████╗
# ██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔════╝
# ██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║   ███████╗
# ██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║   ╚════██║
# ╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║   ███████║
#  ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝
from libqtile import bar, widget, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=15,
    padding=6,
)

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