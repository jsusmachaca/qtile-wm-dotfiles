from libqtile.layout import MonadTall, MonadWide, Max, Bsp
from libqtile.config import Match
from libqtile import layout

configs = {
    "border_focus": "#707070",
    "border_width": 1,
    "margin": 7
}

layouts = [
    MonadTall(**configs),
    MonadWide(**configs),
    Bsp(**configs),
    Max()
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Pavucontrol"), # Pantalla de control de audio
        Match(wm_class="Lxappearance"), # Configuración de temas
        Match(wm_class="Nitrogen"), # Configuracion de fondos de pantalla
        Match(wm_class="Thunar"), # Gestor de archivos
        Match(wm_class="Blueman-manager"), # Gestor de bluetooth
        Match(wm_class="Arandr"), # Gestor de pantallas
        Match(wm_class="Geeqie"), # Gestor de imágenes
    ],
    border_focus="#5d5d5d",
    border_width=1,
)