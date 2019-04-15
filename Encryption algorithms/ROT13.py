def rot13_algorithm(text):
    """
    Takes text and returns it after applying ROT13-algorithm.

    :param text:    Text to be encoded.
    :return:    Encoded text.
    """

    new_text = ""           # Since every encoded letter is appendend, an empty String is created as a base.

    for items in range(0, len(text)):
        val = ord(text[items])          # Unicode code of corresponding letter is saved for comparisons.

        if 96 < val < 123:            # Range for lowercase letters.
            val -= ord("a")
            val += 13
            val %= 26           # Modulo is needed for encoded letters that go beyond 'z' (e.g. s -> f).
            val += ord("a")
        elif 64 < val < 91:             # Range for uppercase letters.
            val -= ord("A")
            val += 13
            val %= 26
            val += ord("A")
        else:
            pass

        new_text = new_text + chr(val)

    return new_text


def menu():
    """
    Menu for navigating application.
    """

    while True:
        print("I want to test this application!")
        user_input = input("[1] En-/Decrypt Text\n[x] End program\n")
        if user_input == "1":
            text = input("\nText:")
            encrypted_text = rot13_algorithm(text)
            print("Text: {}\n".format(encrypted_text))
        elif user_input == "x":
            break
        else:
            pass


if __name__ == "__main__":

    menu()
