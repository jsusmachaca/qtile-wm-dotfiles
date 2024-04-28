from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from .keys import keys, mod


# groups = [Group(i) for i in [" 󰈹  ", " 󰊢  ", "   ", "   ", "   ", "   ",]]

groups = [
    Group(" 󰈹  ", matches=[Match(wm_class=["firefox", "brave-browser", "google-chrome"])]),
    Group(" 󰊢  ", matches=[Match(wm_class=["code",])]),
    Group("   ", matches=[Match(wm_class=['Alacritty',])]),
    Group("   ", matches=[Match(wm_class=["postman", 'sqlitebrowser'])]),
    Group("   ", matches=[Match(wm_class=["thunar", "geeqie", "vlc"])]),
    Group("   ", matches=[Match(wm_class=["obs", "discord"])]),
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
