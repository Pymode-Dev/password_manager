import pyperclip
import random
import sys

from collections import OrderedDict
from string import ascii_letters, punctuation

import command


password_bank = ascii_letters + punctuation


def generate_password(length: int = 8) -> str:
    print("Password generated successfully")
    password = "".join(random.choices(password_bank, k=length))
    pyperclip.copy(password)
    print("Password has been copied")
    return password


def ask_user_to_save_password():
    question: str = input("Do you want to save the password(y/n): ")
    return question

def ask_site_name():
    question: str = input("Name of the site: ")
    return question

def verify_input():
    password_generated = generate_password()
    site_name = ask_site_name()
    user_option = OrderedDict(
            {
                'y': command.SavePassword(site_name, password_generated),
                'n': command.Quit()
            }
            )
    user_option[ask_user_to_save_password()].execute()
