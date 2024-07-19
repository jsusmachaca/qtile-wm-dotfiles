from libqtile.config import Key
from libqtile.lazy import lazy
import os

mod = 'mod4'
terminal = 'alacritty'

keys = [
    # Focus apps.
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize MonadTall
    Key([mod, "control"], "left", lazy.layout.grow()),
    Key([mod, "control"], "right", lazy.layout.shrink()),
    Key([mod], "s", lazy.window.toggle_floating()),
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

#                       CUSTOM
    # Rofi
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "a", lazy.spawn("rofi -show window")),
    Key([mod], "e", lazy.spawn("rofi -show emoji")),
    
    # Screen Capture
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    Key([mod], "r", lazy.spawn("redshift -O 4000")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Audio Control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness Control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
