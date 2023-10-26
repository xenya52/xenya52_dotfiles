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
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        
        wallpaper = "~/.config/qtile/Images/wallpaper.jpg",
        wallpaper_mode = "stretch",

        top=bar.Bar(
            [
                widget.Sep(
                    background="#FC679E",
                    linewidth=0,
                    padding=12,
                ),
                widget.Image(
                    background="#FC679E",
                    filename="~/.config/qtile/Images/lucyProfilePicTransparent.png",
                    scale="true"
                ),
                widget.Systray(
                    background="#FC679E",
                ),
                widget.TextBox(
                    text='',
                    background="#FF77A6",
                    foreground="#FC679E",
                    padding=0,
                    fontsize=42,
                ),
                widget.Clock(
                    background = "#FF77A6",
                    foreground = "#EDA3B1",
                    format = " %d/%m/%Y",
                    update_interval = 60.0,
                ),
                widget.Clock(
                    background = "#FF77A6",
                    foreground = "#000000",
                    format = " %H:%M",
                    update_interval = 60.0,
                ),
                widget.TextBox(
                    text='',
                    background="#FEA3BD",
                    foreground="#FF77A6",
                    padding=0,
                    fontsize=42,
                ), 
                widget.GroupBox(
                    background = "#FEA3BD",
                    inactive = "#FD95B4",
                    active = "#000000",
                    rounded=True,
                    highlight_color="#FEB2C8",
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    foreground="#FEA3BD",
                    padding=0,
                    fontsize=42,
                ),
                widget.Prompt(
                    foreground="#EDA3B1",
                ),
                widget.Spacer(
                ),
                widget.TextBox(
                    text='',
                    foreground="#FEB2C8",
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background="#FEB2C8",
                    foreground="#000000",
                    format="󰘚 {load_percent}%"
                ),
                widget.TextBox(
                    text='',
                    foreground="#FEA3BD",
                    background="#FEB2C8",
                    padding=0,
                    fontsize=42,
                ),
                widget.Memory(
                    format=" {MemUsed: .0f}{mm}",
                    background="#FEA3BD",
                    foreground="#000000",
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#FEA3BD",
                    foreground="#FD95B4",
                    padding=0,
                    fontsize=42
                ),
                widget.Battery(
                    format="󰁺{char} {percent:1.0%} ",
                    charge_char="↑",
                    discharge_char="↓",
                    full_char="!",
                    low_foreground="#FF0001",
                    background="#FD95B4",
                    foreground="#000000",
                ),
                widget.TextBox(
                    text='',
                    background="#FD95B4",
                    foreground="#FE82AC",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=" ",
                    foreground = "#000000",
                    background = "#FE82AC",
                ),
                widget.KeyboardLayout(
                    background="#FE82AC",
                    foreground="#000000",
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background="#FE82AC",
                    foreground="#FF77A6",
                    padding=0,
                    fontsize=42,
                ),
                widget.Backlight(
                    backlight_name = "intel_backlight",
                    format="󰍹 {percent:2.0%} ",
                    background = "#FF77A6",
                    foreground = "#000000",
                    scroll = True,
                ),
                widget.TextBox(
                    text='',
                    background = "#FF77A6",
                    foreground = "#FC679E",
                    padding=0,
                    fontsize=42
                ),
                widget.Volume(
                    background ="#FC679E",
                    foreground ="#000000",
                    fmt=" {} "
                ),
                widget.Sep(
                    background = "#FC679E",
                    linewidth=0,
                    padding=12,
                ),
            ],
            24,
            background = "#32323200",
            margin = [5,5,5,5],
            background_opacity = 0.5,
        ),
    ),
]
