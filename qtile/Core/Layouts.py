# ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗████████╗███████╗
# ██║     ██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
# ██║     ███████║ ╚████╔╝ ██║   ██║██║   ██║   ██║   ███████╗
# ██║     ██╔══██║  ╚██╔╝  ██║   ██║██║   ██║   ██║   ╚════██║
# ███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝   ██║   ███████║
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝
from libqtile import layout
from libqtile.config import Match

layout_conf = {
    "margin":20,
    "border_normal":"EDA3B1",
    "border_focus":"8C367C",
    "border_width":2,   
}

layouts = [
    layout.Max(**layout_conf),
    layout.Columns(**layout_conf),
]