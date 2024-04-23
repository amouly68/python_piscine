import sys

def filter_string(sentence, length):
    return [word for word in sentence.split() if len(word) > length]

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        sentence = sys.argv[1]
        length_input = sys.argv[2]

        if not isinstance(sentence, str) or not length_input.isdigit():
            raise AssertionError("AssertionError: the arguments are bad")
        
        length = int(length_input)

        result = filter_string(sentence, length)
        print(result)
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()