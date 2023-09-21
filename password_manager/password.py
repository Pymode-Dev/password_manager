"""
Python file that manages the actions on password manager
"""

import json
import pyperclip

from rich.table import Table
from rich.console import Console

from encrypter import encrypt
from decrypter import decrypt


def read_json():
    filename = '/home/pymode-dev/my_projects/password_manager/password_manager/password_db.json'
    with open(filename, "r") as file:
        reader = json.load(file)
        return reader["password"]


def write_to_json(data, filepath):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=2)


def save_password(website: str, password: str) -> str:
    """
    This save the password and the site.
    """
    database: dict = read_json()
    database.setdefault(website, encrypt(password))
    data = {"password": database}
    write_to_json(data, "password_db.json")
    return "✔ Data Saved ✔"


def get_user_password(website: str) -> str:
    database: dict = read_json()
    result = database.get(website, None)
    if result is not None:
        pyperclip.copy(decrypt(result))
    return "✔ Copied ✔"


def view_database():
    table = Table()
    console = Console()
    database: dict = read_json()
    table.add_column('Website', style='green')
    table.add_column('Password', style='green')
    for website, password in database.items():
        table.add_row(website, password)
    console.print(table)


def delete_password(website: str) -> str:
    database: dict = read_json()
    try:
        database.pop(website)
    except KeyError:
        return 'Password is not in the database'
    else:
        data = {'password': database}
        write_to_json(data, 'password_db.json')
        return "✔ Deleted ✔"
