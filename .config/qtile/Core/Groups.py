#  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝
# ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗
# ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║
# ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝
from libqtile.config import Key, Group, Match
from libqtile.command import lazy

groups = []

group_names = ["1", "2", "3", "4","5"]
group_labels = ["󰣇 ", " ", " ", "󱓧 "," "]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall","monadtall","monadtall"]

for i in range(len(group_names)):
    groups.append (
        Group (
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
    )
)

