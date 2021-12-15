from argparse import ArgumentParser, Namespace

from cui.game import CUIGame
from gui.game import GUIGame


def main() -> None:
    args = parse_args()
    if args.cui:
        CUIGame().run()
    else:
        GUIGame().run()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--cui", action="store_true", help="play CUI game")
    group.add_argument("-g", "--gui", action="store_true", help="play GUI game")
    return parser.parse_args()


main()
