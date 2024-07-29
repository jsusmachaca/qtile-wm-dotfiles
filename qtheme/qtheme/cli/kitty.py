from os import path
from qtheme.utils.colors import green, red


class Kitty:
    def __init__(self, user_path) -> None:
        self.user_path = user_path

    def set_terminal_theme(self, theme: str = None):
        try:
            kitty_conf_path = path.join(self.user_path, '.config', 'kitty', 'kitty.conf')
            
            if theme is None:
                return
            
            if not path.exists(kitty_conf_path):
                raise FileNotFoundError('The conf file kitty does not exist.')

            with open(kitty_conf_path, 'r+') as file:
                lines = file.readlines()
                for index, line in enumerate(lines):
                    if line.startswith('include themes'):
                        lines[index] = f'include themes/{theme}.conf\n'
                        break
                else:
                    raise ValueError('Theme section not found in Kitty configuration file.')

                file.seek(0)
                file.writelines(lines)
                file.truncate()

            green(f'Kitty terminal theme set to "{theme}".')

        except (FileNotFoundError, ValueError) as e:
            red(f'Error: {e}')
        except Exception as e:
            red(f'Unexpected error: {e}')

    def set_terminal_font(self, font_family: str = None):
        try:
            kitty_conf_path = path.join(self.user_path, '.config', 'kitty', 'kitty.conf')
            
            if font_family is None:
                return
            
            if not path.exists(kitty_conf_path):
                raise FileNotFoundError('The conf file kitty does not exist.')

            with open(kitty_conf_path, 'r+') as file:
                lines = file.readlines()
                for index, line in enumerate(lines):
                    if line.startswith('font_family'):
                        lines[index] = f'font_family {font_family}\n'
                        break
                else:
                    raise ValueError('Theme section not found in Kitty configuration file.')

                file.seek(0)
                file.writelines(lines)
                file.truncate()

            green(f'Kitty terminal font set to "{font_family}".')

        except (FileNotFoundError, ValueError) as e:
            red(f'Error: {e}')
        except Exception as e:
            red(f'Unexpected error: {e}')

    def set_terminal_opacity(self, opacity: str = None):
        try:
            kitty_conf_path = path.join(self.user_path, '.config', 'kitty', 'kitty.conf')
            
            if opacity is None:
                return
            
            if not path.exists(kitty_conf_path):
                raise FileNotFoundError('The conf file kitty does not exist.')

            with open(kitty_conf_path, 'r+') as file:
                lines = file.readlines()
                for index, line in enumerate(lines):
                    if line.startswith('background_opacity'):
                        lines[index] = f'background_opacity {opacity}\n'
                        break
                else:
                    raise ValueError('Theme section not found in Kitty configuration file.')

                file.seek(0)
                file.writelines(lines)
                file.truncate()

            green(f'Kitty terminal opacity set to "{opacity}".')

        except (FileNotFoundError, ValueError) as e:
            red(f'Error: {e}')
        except Exception as e:
            red(f'Unexpected error: {e}')