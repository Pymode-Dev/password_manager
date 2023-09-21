#! /usr/bin/env python3

import argparse

from collections import OrderedDict

from __init__ import __version__
import command


class Options:
    def __init__(self, command) -> None:
        self.command = command

    def choose_option(self) -> None:
        self.command.execute()


def get_website(parser) -> str:
    return parser.website if "website" in parser else None


def get_password(parser) -> str:
    return parser.password if "password" in parser else None


def main():
    """
    The main function.
    """
    args = parse_cmd_arguments()
    website = get_website(args)
    password = get_password(args)

    option = OrderedDict({
        "save": Options(command.SavePassword(website, password)),
        "copy": Options(command.GetPassword(website)),
        "delete": Options(command.DeletePassword(website)),
        "view": Options(command.ViewPassword()),
        "gen": Options(command.GeneratePassword()),
    })
    option[args.command].choose_option()


def parse_cmd_arguments():
    parser = argparse.ArgumentParser(
        prog="Command Line Password Manager",
        description="CMD Password Manager, This manage your password using command line.\n"
                    "You can: save, auto copy to clipboard, delete password, and you can also update",
        epilog="Thanks for using Command Line Password Manager.",
    )
    sub_parser = parser.add_subparsers(dest="command")
    parser.version = f"CMD Password Manager v{__version__}"
    parser.add_argument("-v", "--version", action="version")

    copies = sub_parser.add_parser("copy")
    save = sub_parser.add_parser("save")
    delete = sub_parser.add_parser("delete")
    view = sub_parser.add_parser("view")
    gen = sub_parser.add_parser("gen")

    copies.add_argument("website", type=str, help="Copy your password")
    save.add_argument("website", type=str, )
    save.add_argument("password", type=str, )
    delete.add_argument("website", type=str,)

    return parser.parse_args()


if __name__ == "__main__":
    main()
