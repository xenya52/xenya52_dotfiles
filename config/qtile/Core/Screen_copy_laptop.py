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
    font="Terminus",
    fontsize=15,
    padding=1,
)
extension_defaults = widget_defaults.copy()

def mail_shortcut():
    lazy.spawn("thunderbird")
    lazy.spawn("obsidian")
    lazy.spawn("firefox https://calendar.google.com/calendar/u/0/r/tasks?pli=1")
    lazy.spawn("firefox https://calendar.google.com/calendar/u/0/r?pli=1")

screens = [
    #ScreenOne
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
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/mail.png',
                    margin_y=3,
                    background=violet2,
                    mouse_callbacks={"Button1":lazy.spawn("thunderbird")},
                ),
                #CurrentDate
                widget.Clock(
                    background = violet2,
                    foreground =  textColor_dark,
                    format = "%d-%m-%Y/%H:%M",
                    update_interval = 60.0,
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                ), 
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/temperature.png',
                    margin_y=3,
                    background=violet3,
                    mouse_callbacks={"Button1":lazy.spawn("kitty curl wttr.in/Regensburg sleep 10")}
                ),
                #Weather
                widget.OpenWeather(
                    background=violet3,
                    foreground=textColor_dark,
                    location='Regensburg', 
                    format='{main_temp}°{units_temperature} {humidity}%',
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20,
                ), 
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/ram.png',
                    margin_y=3,
                    background=violet4,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu "),}
                ),
                #Memory
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background=violet4,
                    foreground=textColor_dark,
                    interval=1.0,
                    
                ),
                
                widget.TextBox(
                    text='',
                    background=violet5,
                    foreground=violet4,
                    padding=0,
                    fontsize=20,
                ), 
                widget.Image(
                    margin_y=3,
                    filename='~/.config/qtile/Images/bar_icons/cpu.png',
                    background=violet5,
                    mouse_callbacks={"Button1":lazy.spawn("kitty bpytop"),}
                ),
                widget.CPU(
                    background=violet5,
                    foreground=textColor_dark,
                    format="{load_percent}%",
                ),
                widget.ThermalZone(
                    background=violet5,
                    fgcolor_normal=textColor_dark,
                    fgcolor_high=textColor_dark
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet5,
                    padding=0,
                    fontsize=20,
                ),

                widget.Spacer(),


                widget.Systray(),
                widget.TextBox(
                    text='',
                    foreground=violet5,
                    padding=0,
                    fontsize=20
                ),
                #Choosen Layout
                widget.CurrentLayout(
                    background = violet5,
                    foreground = textColor_dark,
                ),
                widget.TextBox(
                    text='',
                    foreground=violet4,
                    background=violet5,
                    padding=0,
                    fontsize=20,
                ),
                #Groups
                widget.GroupBox(
                    background = violet4,
                    inactive = violet3,
                    active = textColor_dark,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20
                ),
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/keyboard.png',
                    margin_y=3,
                    background=violet3,
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
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/desktop.png',
                    margin_y=3,
                    background=violet2,
                ),
                widget.Backlight(
                    backlight_name = "intel_backlight",
                    format="{percent:2.0%} ",
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
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/volume.png',
                    margin_y=3,
                    background=violet1,
                ),
                widget.Volume(
                    background = violet1,
                    foreground = textColor_dark,
                    fmt="{}"
                ),
                widget.Sep(
                    background = violet1,
                    linewidth=0,
                    padding=6,
                ),
            ],
            22,
            background = "aa698b",
            #border_width = [0,0,2,0],
            #border_color = violet1,
            #margin = [5,5,0,5],
            #background_opacity = 0.5,
        ),
    ),
    #ScreenTwo
    Screen(
        
        wallpaper = "~/.config/qtile/Images/wallpaperPixel.jpg",
        wallpaper_mode = "stretch",

        top=bar.Bar(
            [
                widget.Spacer(),

                widget.TextBox(
                    text='',
                    foreground=violet5,
                    padding=0,
                    fontsize=20
                ),
                #Choosen Layout
                widget.CurrentLayout(
                    background = violet5,
                    foreground = textColor_dark,
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet4,
                    background=violet5,
                    padding=0,
                    fontsize=20,
                ),
                #Groups
                widget.GroupBox(
                    background = violet4,
                    inactive = violet3,
                    active = textColor_dark,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
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
            background = "aa698b",
            #border_width = [0,0,2,0],
            #border_color = violet1,
            #margin = [5,5,0,5],
            #background_opacity = 0.5,
        ),
    ),
]
