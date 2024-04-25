import sys
from ft_filter import ft_filter

def main():
    if len(sys.argv) != 1:
        raise AssertionError("AssertionError: no arguments for this tester")

    # Test avec une liste d'entiers
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_nums = ft_filter(lambda x: x % 2 == 0, nums)
    expected_result = list(filter(lambda x: x % 2 == 0, nums))  
    print(f"Test ft_filter with nums:")
    print(f"Input: {nums}")
    print(f"Expected result: {expected_result}")
    print(f"ft_filter result: {filtered_nums}")
    assert filtered_nums == expected_result, f"Test failed for nums: expected {expected_result}, got {filtered_nums}"

    # Test avec une liste de chaînes de caractères
    words = ["apple", "banana", "orange", "grape", "kiwi"]
    filtered_words = ft_filter(lambda x: len(x) > 5, words)
    expected_result = list(filter(lambda x: len(x) > 5, words)) 
    print(f"\nTest ft_filter with words:")
    print(f"Input: {words}")
    print(f"Expected result: {expected_result}")
    print(f"ft_filter result: {(filtered_words)}")
    assert (filtered_words) == expected_result, f"Test failed for words: expected {expected_result}, got {filtered_words}"

    print("\nAll tests passed successfully.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
