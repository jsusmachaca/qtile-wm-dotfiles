import subprocess
from os import path
from libqtile import hook
from settings.keys import keys, mod
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.screens import screens
from settings.mouse import mouse
from settings.widgets import widget_defaults, extension_defaults


@hook.subscribe.startup_once
def start_once():
    home = path.expanduser('~')
    subprocess.call([path.join(home, '.config', 'qtile', 'autostart.sh')])

# Drag floating layouts.

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"