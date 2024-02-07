#  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝
# ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗
# ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║
# ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝
from libqtile.config import Key, Group, Match
from libqtile.command import lazy

groups = []

group_names = ["1", "2", "3", "4"]
group_labels = ["[ぜ]", "[に]", "[ぁ]", "[:D]"]
group_layouts = ["tile", "tile", "tile", "tile"]

for i in range(len(group_names)):
    groups.append (
        Group (
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
    )
)

