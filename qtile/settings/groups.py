from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from .keys import keys, mod
from re import compile


# groups = [Group(i) for i in [" 󰈹  ", " 󰊢  ", "   ", "   ", "   ", "   ",]]

groups = [
    Group(" 󰈹  ", matches=[Match(wm_class=compile(r"^(firefox|brave-browser|google-chrome)$"))]),
    Group(" 󰊢  ", matches=[Match(wm_class=compile(r"^(code)$"))]),
    Group("   ", matches=[]),
    Group("   ", matches=[Match(wm_class=compile(r"^(postman|sqlitebrowser)"))]),
    Group("   ", matches=[Match(wm_class=compile(r"^(thunar|geeqie|vlc)"))]),
    Group("   ", matches=[Match(wm_class=compile(r"^(obs|discord)"))]),
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
            Key([mod, "control"], actual_key, lazy.window.togroup(group.name, switch_group=False)),
        ]
    )
