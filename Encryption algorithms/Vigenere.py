import sys
import random


def vigenere_algorithm(text, code, j=0):
    """
    Takes text and returns it after applying vigenere algorithm.

    :param text:    Text to be encoded.
    :param code:    Keyword used for encryption.
    :param j:   Variable to cycle through the keyword.
    :return:    Encoded text.
    """

    new_text = ""           # Since every encoded letter is appendend, an empty String is created as a base.

    for i in range(0, len(text)):           # Runs through every letter of the text individually.
        val = ord(text[i])
        code_val = ord(code[j])

        if 96 < val < 123:            # Range for lowercase letters.
            val -= ord("a")
            if code_val > 96:
                code_val -= ord("a")
            else:
                code_val -= ord("A")
            val += code_val
            val %= 26
            val += ord("a")
        elif 64 < val < 91:         # Range for uppercase letters.
            val -= ord("A")
            if code_val > 96:
                code_val -= ord("a")
            else:
                code_val -= ord("A")
            val += code_val
            val %= 26
            val += ord("A")
        else:
            j -= 1

        new_text = new_text + chr(val)

        j += 1
        if j == len(code):
            j = 0

    return new_text


def code_generator(length):
    """
    Generates a random keyword.

    :param length:  Length of the keyword.
    :return:    Keyword.
    """

    code = ""
    key_num = random.SystemRandom()
    for items in range(0, length):
        case = key_num.randint(1,2)
        if case == 1:
            code += (chr(key_num.randint(65, 90)))
        elif case == 2:
            code += (chr(key_num.randint(97, 122)))

    return code


def menu():
    """
    Menu for navigating application.
    """

    while True:
        user_input = input("[1] Encrypt Text\n[x] End program\n\n")
        if user_input == "1":
            text = input("\nText:\n> ")
            code = input("Code (leave blank if you want an random one): ")
            if code == "":
                code = code_generator(len(text))
            encrypted_text = vigenere_algorithm(text, code)
            print("\nRaw text: {}".format(text))
            print("Code: {}".format(code))
            print("Encrypted text: {}".format(encrypted_text))
            print()
        elif user_input == "x":
            break
        else:
            pass


if __name__ == "__main__":

    menu()
