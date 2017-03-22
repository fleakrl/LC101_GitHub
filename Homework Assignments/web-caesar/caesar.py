def encrypt(text, rot):
    encrypted_string = ""

    # Rotate each character in the user inputted text by the rotation amount & store it in a new encrypted string
    for char in text:
        encrypted_string += rotate_character(char, rot)

    return encrypted_string


def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - ord('A')
    else:
        return ord(letter) - ord('a')


def rotate_character(char, rot):
    # return the character if it is not an alpha character
    if not char.isalpha():
        return char

    # find the position of the new character in the alphabet after rotation
    new_character_position = (alphabet_position(char) + rot) % 26

    # preserve the case of the initial character & return the new character
    if char.isupper():
        new_char = chr(ord("A") + new_character_position)
    else:
        new_char = chr(ord("a") + new_character_position)
    return new_char
