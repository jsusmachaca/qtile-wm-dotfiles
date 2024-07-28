#!/usr/bin/env python3

from os import path, listdir
from colors import red, yelow, green, imagenta
from cli import cli
from argparse import ArgumentParser


user_path = path.expanduser('~')

def main ():
    try:
        kt = cli(user_path)
        parser = ArgumentParser()
        parser.add_argument('-ls', '--list', action='store_true', help='List available themes')
        parser.add_argument('-t', dest='theme', help='Theme to set', metavar='theme')
        parser.add_argument('-p', dest='position', help='Position of the qtile bar [top/bottom] or [t/b]', metavar='position')

        group = parser.add_argument_group('Terminal options')
        group.add_argument('-T', dest='terminal', help='Theme to set for Kitty terminal', metavar='terminal-theme')
        group.add_argument('-Tf', dest='terminal-font', help='Font to set fot Kitty Terminal', metavar='terminal-font')
        args = parser.parse_args()

        if args.list:
            if args.theme or args.position:
                parser.error('The command --list does not accept addicional arguments')
            kt.menu_themes()
            return

        kt.set_qtile_theme(args.theme)
        kt.set_bar_position(args.position)
        kt.set_terminal_theme(args.terminal)

    except Exception as e:
        red(f'Unexpected error: {e}')


if __name__ == '__main__':
    main()