from libqtile import bar, widget
from libqtile.config import Screen
import json
import os


def set_theme():
    user_path = os.path.expanduser('~')
    full_path = os.path.join(user_path, '.config', 'qtile', 'themes', 'theme_selector.json')
    with open(full_path, 'r') as file:
        json_theme = json.load(file)
        theme_path = os.path.join(user_path, '.config', 'qtile', 'themes', json_theme['theme'] + '.json')
        
        with open(theme_path) as json_file:
            global data
            data = json.load(json_file)

set_theme()

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
#       WIDGETS ARCH LOGO    .
                widget.TextBox(
                    text='   ',
                    foreground=data["arch_logo"]["foreground"],
                    background=data['bar'],
                    fontsize=22,
                ),

                widget.Sep(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=data['bar']
                ),

                widget.Spacer(
                    length=20,
                    background=data['bar'],
                ),

#       WIDGETS GROUPS     .
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=data['bar'],
                    font='UbuntuMono Nerd Font',
                    fontsize=20,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#525050", "#525050"],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=data['current_window']['this_current_screen_border'],
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=data['bar'],
                    other_screen_border=data['bar'],
                ),

                widget.WindowName(
                    foreground=data['window_name']['foreground'],
                    background=data['bar'],
                ),

                widget.Sep(
                    background=data['bar'],
                    foreground=data['bar'],
                ),


#                                   WIDGETS RIGHT BAR                 .

#       WIDGETS UPDATES     .
                widget.TextBox(
                    text="󱈙 ",
                    padding=-10.5,
                    fontsize=37,
                    foreground=data['bar'],
                    background=data['widget_update']['arrow']['background'],
                ),

                widget.TextBox(
                    text=" ",
                    foreground=data['widget_update']['icon']['foreground'],
                    background=data['widget_update']['icon']['background'],
                ),

                widget.CheckUpdates(
                    foreground=data['widget_update']['checkupdates']['foreground'],
                    background=data['widget_update']['checkupdates']['background'],

                    display_format='{updates}',
                    colour_have_updates=data['widget_update']['checkupdates']['foreground'],
                    custom_command='checkupdates',
                    update_interval=1900,
                ),


#       WIDGETS MEMORY   .
                widget.TextBox(
                    text="󱈙 ",
                    padding=-12,
                    fontsize=37,
                    foreground=data['widget_memory']['arrow']['foreground'],
                    background=data['widget_memory']['arrow']['background'],
                ),

                widget.TextBox(
                    text='󰍛 ',
                    foreground=data['widget_memory']['icon']['foreground'],
                    background=data['widget_memory']['icon']['background'],
                ),

                widget.Memory(
                    format="{MemUsed:.0f}{mm} / {MemTotal:.0f}{mm}",
                    foreground=data['widget_memory']['memory']['foreground'],
                    background=data['widget_memory']['memory']['background'],
                ),

                widget.Sep(
                    foreground=data['widget_memory']['sep']['foreground'],
                    background=data['widget_memory']['sep']['background'],
                ),

#       WIDGETS LAYOUT    .
                widget.TextBox(
                    text="󱈙 ",
                    padding=-12,
                    fontsize=37,
                    foreground=data['widget_layout']['arrow']['foreground'],
                    background=data['widget_layout']['arrow']['background'],
                ),

                widget.CurrentLayoutIcon(
                    scale = 0.6,
                    background=data['widget_layout']['layout_icon']['background'],
                ),

                widget.CurrentLayout(
                    foreground=data['widget_layout']['layout']['foreground'],
                    background=data['widget_layout']['layout']['background'],
                ),

#       WIDGETS CLOCK   . 
                widget.TextBox(
                    text="󱈙 ",
                    padding=-12,
                    fontsize=37,
                    foreground=data['widget_clock']['arrow']['foreground'],
                    background=data['widget_clock']['arrow']['background'],
                ),

                widget.TextBox(
                    text='󰃰 ',
                    foreground=data['widget_clock']['icon']['foreground'],
                    background=data['widget_clock']['icon']['background'],
                ),

                widget.Clock(
                    format="%d/%m/%Y ",
                    foreground=data['widget_clock']['clock']['foreground'],
                    background=data['widget_clock']['clock']['background'],
                ),

                widget.Sep(
                    foreground=data['widget_clock']['sep']['foreground'],
                    background=data['widget_clock']['sep']['background'],
                ),

                widget.Clock(
                    format=" %I:%M %p",
                    foreground=data['widget_clock']['clock']['foreground'],
                    background=data['widget_clock']['clock']['background'],
                ),

                widget.Sep(
                    foreground=data['widget_clock']['sep_f']['color'],
                    background=data['widget_clock']['sep_f']['color'],
                ),

#       WIDGETS SYSTRAY   
                widget.TextBox(
                    text="󱈙 ",
                    padding=-11,
                    fontsize=37,
                    foreground=data['systray']['arrow']['foreground'],
                    background=data['bar'],
                ),
                
                widget.Systray(
                    background=data['bar'],
                ),
            ],
            21,
            opacity=0.99,
        ),
    ),
]
