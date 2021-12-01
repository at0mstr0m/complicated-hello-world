from string import ascii_letters, whitespace, punctuation
import re


def main():
    needed_letters = re.compile('[delorwH /!]')
    alphabet = ascii_letters + whitespace[0] + punctuation[0]
    letters = [letter for letter in alphabet if needed_letters.match(letter)]
    indexes = [6, 1, 2, 2, 3, 7, 5, 3, 4, 2, 0, -1]
    print("".join(letters[index] for index in indexes))


if __name__ == '__main__':
    main()
