#   _____                              
#  / ____|                             
# | (___   ___ _ __ ___  ___ _ __  ___ 
#  \___ \ / __| '__/ _ \/ _ \ '_ \/ __|
#  ____) | (__| | |  __/  __/ | | \__ \
# |_____/ \___|_|  \___|\___|_| |_|___/
                                      
                                      
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
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/mail.png',
                    background=violet1,
                    mouse_callbacks={"Button1":lazy.spawn(mail_shortcut)},
                ),
                #CurrentDate
                widget.Clock(
                    background = violet1,
                    foreground =  textColor_dark,
                    format = "%d-%m-%Y/%H:%M",
                    update_interval = 60.0,
                    mouse_callbacks={"Button1":lazy.spawn("obsidian"),}
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ), 
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/temperature.png',
                    background=violet2,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu "),}
                ),
                #Weather
                widget.OpenWeather(
                    background=violet2,
                    foreground=textColor_dark,
                    location='Regensburg', 
                    format='{main_temp}°{units_temperature} {humidity}%',
                    mouse_callbacks={"Button1":lazy.spawn("kitty curl wttr.in/Regensburg sleep 10")}
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ), 
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/ram.png',
                    background=violet3,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu "),}
                ),
                #Memory
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background=violet3,
                    foreground=textColor_dark,
                    interval=1.0,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu /"),}
                ),
                
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ), 
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/cpu.png',
                    background=violet4,
                    mouse_callbacks={"Button1":lazy.spawn("kitty bpytop"),}
                ),
                widget.CPU(
                    background=violet4,
                    foreground=textColor_dark,
                    format="{load_percent}%",
                    mouse_callbacks={"Button1":lazy.spawn("kitty bpytop"),}
                ),
                widget.ThermalZone(
                    background=violet4,
                    fgcolor_normal=textColor_dark,
                    fgcolor_high=textColor_dark,
                    format="{temp}°C"
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet4,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono",
                ),

                widget.Spacer(),

                widget.Systray(),

                widget.TextBox(
                    text='',
                    foreground=violet4,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ),
                #Choosen Layout
                widget.CurrentLayout(
                    background = violet4,
                    foreground = textColor_dark,
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet3,
                    background=violet4,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ),
                #Groups
                widget.GroupBox(
                    background = violet3,
                    inactive = violet2,
                    active = textColor_dark,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ),
                widget.TextBox(
                    text="",
                    foreground = textColor_dark,
                    background = violet2,
                ),
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/keyboard.png',
                    background=violet2,
                ),
                widget.KeyboardLayout(
                    background=violet2,
                    foreground=textColor_dark,
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                    font="JetBrainsMono"
                ),
                widget.Image(
                    filename='~/.config/qtile/Images/bar_icons/volume.png',
                    background=violet1,
                ),
                widget.Volume(
                    background = violet1,
                    foreground = textColor_dark,
                    fmt="{} "
                ),
                widget.Sep(
                    background = violet1,
                    linewidth=0,
                    padding=6,
                ),
            ],
            18,
            background = "aa698b",
            #border_width = [0,0,2,0],
            #border_color = violet1,
            #margin = [5,5,0,5],
            #background_opacity = 0.5,
        ),
    ),

]
