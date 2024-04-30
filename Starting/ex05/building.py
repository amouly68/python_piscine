import sys


def count_chars(text) -> dict:
    """
    Count the number of upper and lower case letters,
    punctuation marks, spaces, and digits in the given text.
    args:   text: a string
    return: a dict with the counts of each category
    """
    counts = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0
    }

    for char in text:
        if char.isupper():
            counts["upper letters"] += 1
        elif char.islower():
            counts["lower letters"] += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            counts["punctuation marks"] += 1
        elif char.isspace() or char == "\n":
            counts["spaces"] += 1
        elif char.isdigit():
            counts["digits"] += 1

    return counts


def main():
    text = ""
    if len(sys.argv) > 2:
        raise AssertionError("AssertionError: only one argument is required")
    if len(sys.argv) == 2:
        text = sys.argv[1]

    if not text:
        print("What is the text to count?")
        text = sys.stdin.read()

    counts = count_chars(text)

    total_chars = sum(counts.values())
    print(f"The text contains {total_chars} characters:")
    for category, count in counts.items():
        print(f"{count} {category}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
