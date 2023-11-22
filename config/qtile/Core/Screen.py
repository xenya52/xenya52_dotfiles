# ██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗███████╗
# ██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔════╝
# ██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║   ███████╗
# ██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║   ╚════██║
# ╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║   ███████║
#  ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝
from libqtile import bar, widget, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from Core.Colors import violet1, violet2, violet3, violet4, violet5, violet6, textColor_dark

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=15,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        
        wallpaper = "~/.config/qtile/Images/wallpaperPixel.jpg",
        wallpaper_mode = "stretch",

        top=bar.Bar(
            [
                widget.Sep(
                    background=violet1,
                    linewidth=0,
                    padding=6,
                ),
                widget.Battery(
                    format="{char}{percent:1.0%}",
                    charge_char="↑",
                    discharge_char="↓",
                    full_char="!",
                    low_foreground="#FF0001",
                    background=violet1,
                    foreground=textColor_dark,
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                ),

                #CurrentDate
                widget.Clock(
                    background = violet2,
                    foreground =  textColor_dark,
                    format = "%d-%m-%Y/%H:%M",
                    update_interval = 60.0,
                    mouse_callbacks={"Button1":lazy.spawn("obsidian"),}
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                ),
                widget.Wlan(
                    format='',
                    background=violet3,
                    foreground=textColor_dark,
                    mouse_callbacks={"Button1":lazy.spawn("kitty nmtui"),}
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20,
                ), 
                #Weather
                widget.OpenWeather(
                    background=violet4,
                    foreground=textColor_dark,
                    location='Regensburg', 
                    format='{icon}{main_temp}°{units_temperature} {humidity}%',
                    mouse_callbacks={"Button1":lazy.spawn("kitty curl wttr.in/Regensburg sleep 10")}
                ),
                widget.TextBox(
                    text='',
                    background=violet5,
                    foreground=violet4,
                    padding=0,
                    fontsize=20,
                ), 
                #Memory
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background=violet5,
                    foreground=textColor_dark,
                    interval=1.0,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu /"),}
                ),
                
                widget.TextBox(
                    text='',
                    background=violet6,
                    foreground=violet5,
                    padding=0,
                    fontsize=20,
                ), 

                widget.CPU(
                    background=violet6,
                    foreground=textColor_dark,
                    format="󰘚 {load_percent}%",
                    mouse_callbacks={"Button1":lazy.spawn("kitty bpytop"),}
                ),
                widget.ThermalZone(
                    background=violet6,
                    fgcolor_normal=textColor_dark,
                    fgcolor_high=textColor_dark
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet6,
                    padding=0,
                    fontsize=20,
                ), 

                #Prompts
                widget.Prompt(
                    foreground = violet6,
                ),
                widget.Spacer(
                ),
                widget.Systray(

                ),
                widget.TextBox(
                    text='',
                    foreground=violet6,
                    padding=0,
                    fontsize=20
                ),
                #Choosen Layout
                widget.CurrentLayout(
                    background = violet6,
                    foreground = textColor_dark,
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet5,
                    background=violet6,
                    padding=0,
                    fontsize=20,
                ),
                #Groups
                widget.GroupBox(
                    background = violet5,
                    inactive = violet4,
                    active = textColor_dark,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    background=violet5,
                    foreground=violet4,
                    padding=0,
                    fontsize=20
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=textColor_dark,
                    mouse_callbacks={"Button1":lazy.spawn("rofi -show drun"),}
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20
                ),
                widget.TextBox(
                    text=" ",
                    foreground = textColor_dark,
                    background = violet3,
                ),
                widget.KeyboardLayout(
                    background=violet3,
                    foreground=textColor_dark,
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                ),
                widget.Backlight(
                    backlight_name = "intel_backlight",
                    format="󰍹 {percent:2.0%} ",
                    background = violet2,
                    foreground = textColor_dark,
                ),
                widget.TextBox(
                    text='',
                    background = violet2,
                    foreground = violet1,
                    padding=0,
                    fontsize=20
                ),
                widget.Volume(
                    background = violet1,
                    foreground = textColor_dark,
                    fmt=" {} "
                ),
                widget.Sep(
                    background = violet1,
                    linewidth=0,
                    padding=6,
                ),
            ],
            22,
            background = "00000000",
            #border_width = [0,0,2,0],
            #border_color = violet1,
            #margin = [10,10,0,10],
            #background_opacity = 0.5,
        ),
    ),
]
