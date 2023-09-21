"""
This is a Decrypting algorithm base on
Caesar Cipher Algorithm
"""

import string

CONTAINER: str = string.ascii_letters + string.digits + string.punctuation


def decrypt(password: str, key=15) -> str:
    decrypter: str = ''
    for letter in password:
        value_of_letter = CONTAINER.index(letter)
        decrypter += CONTAINER[value_of_letter - key]

    return decrypter
