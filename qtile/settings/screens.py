from libqtile import bar
from libqtile.config import Screen
from .widgets import main_widgets, secondary_widgets
import subprocess
import json
import os


def set_theme ():
    user_path = os.path.expanduser('~')
    full_path = os.path.join(user_path, '.config', 'qtile', 'themes', 'theme_selector.json')
    with open(full_path, 'r') as file:
        json_theme = json.load(file)
        theme_path = os.path.join(user_path, '.config', 'qtile', 'themes', json_theme['theme'] + '.json')
        
        with open(theme_path) as json_file:
            data = json.load(json_file)
    return json_theme, data

set_theme()

def status_bar (widgets, data):
    return Screen(
        **{bar_placement: bar.Bar(
            widgets(data),
            21,
            opacity=0.99,
        )}
    )

json_theme, data = set_theme()
bar_placement = json_theme.get('position')

screens = [status_bar(main_widgets, data)]

command = subprocess.run(
    'xrandr | grep -w "connected" | cut -d " " -f 2 | wc -l',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    monitors = 1
else:
    monitors = int(command.stdout.decode('UTF-8'))

for i in range(1, monitors):
    screens.append(status_bar(secondary_widgets, data))
