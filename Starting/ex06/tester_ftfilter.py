import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 1:
        raise AssertionError("AssertionError: no arguments for this tester")

    # Test avec une fonction non callable
    # ft_filter(123, [1, 2, 3])

    # Test avec une liste d'entrées non itérable
    # ft_filter(lambda x: x % 2 == 0, 123)

    # Test avec une fonction qui ne renvoie pas un booléen
    # ft_filter(lambda x: x * 2, [1, 2, 3])

    # Test avec une liste d'entiers
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_nums = ft_filter(lambda x: x % 2 == 0, nums)
    expected_result = list(filter(lambda x: x % 2 == 0, nums))
    print("Test ft_filter with nums:")
    print(f"Input: {nums}")
    print(f"Expected result: {expected_result}")
    print(f"ft_filter result: {filtered_nums}")
    if (filtered_nums != expected_result):
        print(f"expected {expected_result}")
        print(f"got {filtered_nums}")
        raise AssertionError("Test failed for nums!")

    # Test avec une liste de chaînes de caractères
    words = ["apple", "banana", "orange", "grape", "kiwi"]
    filtered_words = ft_filter(lambda x: len(x) > 5, words)
    expected_result = list(filter(lambda x: len(x) > 5, words))
    print("\nTest ft_filter with words:")
    print(f"Input: {words}")
    print(f"Expected result: {expected_result}")
    print(f"ft_filter result: {(filtered_words)}")
    if (filtered_nums != expected_result):
        print(f"expected {expected_result}")
        print(f"got {filtered_nums}")
        raise AssertionError("Test failed for words!")

    # Test avec none
    list_with_none = [1, 2, 3, None, 5, 6, 7, "", 9, 10]
    filtered_none = ft_filter(None, list_with_none)
    expected_result = list(filter(None, list_with_none))
    print("\nTest ft_filter with none:")
    print(f"Input: {None}")
    print(f"Expected result: {expected_result}")
    print(f"ft_filter result: {filtered_none}")
    if (filtered_nums != expected_result):
        print(f"expected {expected_result}")
        print(f"got {filtered_nums}")
        raise AssertionError("Test failed for none!")

    print("\nAll tests passed successfully.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occured: {e}")
