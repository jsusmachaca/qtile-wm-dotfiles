from libqtile import widget


widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def arch_logo (data):
    return [
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
    ]

def groupbox (data):
    return [
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
    ]

def checkupdates (data):
    return [
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
            background=data['widget_update']['arrow']['background'],
        ),
        widget.CheckUpdates(
            foreground=data['widget_update']['checkupdates']['foreground'],
            background=data['widget_update']['arrow']['background'],

            display_format='{updates}',
            colour_have_updates=data['widget_update']['checkupdates']['foreground'],
            custom_command='checkupdates',
            update_interval=1900,
        ),
    ]

def memory_state (data):
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-12,
            fontsize=37,
            foreground=data['widget_update']['arrow']['background'],
            background=data['widget_memory']['arrow']['background'],
        ),
        widget.TextBox(
            text='󰍛 ',
            foreground=data['widget_memory']['icon']['foreground'],
            background=data['widget_memory']['arrow']['background'],
        ),
        widget.Memory(
            format="{MemUsed:.0f}{mm} / {MemTotal:.0f}{mm}",
            foreground=data['widget_memory']['memory']['foreground'],
            background=data['widget_memory']['arrow']['background'],
        ),
        widget.Sep(
            foreground=data['widget_memory']['arrow']['background'],
            background=data['widget_memory']['arrow']['background'],
        ),
    ]

def current_layout (data):
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-12,
            fontsize=37,
            foreground=data['widget_memory']['arrow']['background'],
            background=data['widget_layout']['arrow']['background'],
        ),
        widget.CurrentLayoutIcon(
            scale = 0.6,
            background=data['widget_layout']['arrow']['background'],
        ),
        widget.CurrentLayout(
            foreground=data['widget_layout']['layout']['foreground'],
            background=data['widget_layout']['arrow']['background'],
        ),
    ]

def time_date (data):
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-12,
            fontsize=37,
            foreground=data['widget_layout']['arrow']['background'],
            background=data['widget_clock']['arrow']['background'],
        ),
        widget.TextBox(
            text='󰃰 ',
            foreground=data['widget_clock']['icon']['foreground'],
            background=data['widget_clock']['arrow']['background'],
        ),
        widget.Clock(
            format="%d/%m/%Y ",
            foreground=data['widget_clock']['clock']['foreground'],
            background=data['widget_clock']['arrow']['background'],
        ),
        widget.Sep(
            foreground=data['widget_clock']['sep']['foreground'],
            background=data['widget_clock']['arrow']['background'],
        ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=data['widget_clock']['clock']['foreground'],
            background=data['widget_clock']['arrow']['background'],
        ),
        widget.Sep(
            foreground=data['widget_clock']['arrow']['background'],
            background=data['widget_clock']['arrow']['background'],
        ),
    ]

def system_tray (data):
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-11,
            fontsize=37,
            foreground=data['widget_clock']['arrow']['background'],
            background=data['bar'],
        ),
        widget.Systray(
            background=data['bar'],
        ),
    ]

def main_widgets (data: dict):
    return (
        arch_logo(data) +
        groupbox(data) +
        checkupdates(data) +
        memory_state(data) +
        current_layout(data) +
        time_date(data) +
        system_tray(data)
    )

def secondary_widgets (data: dict):
    return (
        arch_logo(data) +
        groupbox(data)[::-1]
    )