import sys

from rich.console import Console

import password

from password_gen import verify_input

class SavePassword:
    def __init__(self, website: str, password: str) -> None:
        self.website = website
        self.password = password

    def execute(self):
        console = Console(style="green")
        message = password.save_password(self.website, self.password)
        console.print(message)


class GetPassword:
    def __init__(self, website: str) -> None:
        self.website = website

    def execute(self) -> None:
        console = Console(style="blue")
        message = password.get_user_password(self.website)
        console.print(message)


class DeletePassword:
    def __init__(self, website: str) -> str:
        self.website = website

    def execute(self) -> None:
        console = Console(style="red")
        message = password.delete_password(self.website)
        console.print(message)


class ViewPassword:
    def execute(self) -> None:
        password.view_database()

class GeneratePassword:
    def execute(self) -> None:
        verify_input()

class Quit:
    def execute(self) -> None:
        sys.exit(0)
