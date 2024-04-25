import sys


def alnum_or_space(s) -> bool:
    """
    Check if a string contains only alphanumeric characters and spaces.
    args:
        s: string
    return: bool
    """
    for c in s:
        if not c.isalnum() and c != " ":
            return False
    return True


def main():
    NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        "0": "-----", "a": ".-", "b": "-...", "c": "-.-.",
        "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
        "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
        "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
        "x": "-..-", "y": "-.--", "z": "--..", " ": "/ ",
    }

    if len(sys.argv) != 2:
        raise AssertionError("AssertionError: the arguments are bad")
    if not isinstance(sys.argv[1], str):
        raise AssertionError("AssertionError: the arguments are bad")
    if not alnum_or_space(sys.argv[1]):
        raise AssertionError("AssertionError: the arguments are bad")

    morse = ""
    for c in sys.argv[1]:
        morse += NESTED_MORSE[c]
    print(morse)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
