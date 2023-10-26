# ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗████████╗███████╗
# ██║     ██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
# ██║     ███████║ ╚████╔╝ ██║   ██║██║   ██║   ██║   ███████╗
# ██║     ██╔══██║  ╚██╔╝  ██║   ██║██║   ██║   ██║   ╚════██║
# ███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝   ██║   ███████║
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝
from libqtile import layout
from libqtile.config import Match

layout_conf = {
    "margin":10,
    "border_normal":"EDA3B1",
    "border_focus":"EDA3B1",
    "border_width":2,   
}

layouts = [
    layout.Max(**layout_conf),
    layout.Columns(**layout_conf),
]

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