"""
This is an Encrypting Algorithm base on
Caesar Cipher Algorithm.
"""

import string

CONTAINER: str = string.ascii_letters + string.digits + string.punctuation


def encrypt(password: str, key=15) -> str:
    encrypter: str = ''
    for letter in password:
        value_of_letter = CONTAINER.index(letter)
        index = value_of_letter + key
        if index > len(CONTAINER):
            index -= len(CONTAINER)
            encrypter += CONTAINER[index]
        else:
            encrypter += CONTAINER[index]

    return encrypter
