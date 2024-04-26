from array2D import slice_me

# Test case 1: Normal case
family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

family1 = [
    [1.80, 78.4],
    [2.15, 102.7, 1.88, 75.2],
    [2.10, 98.5]
]

print("Test case 1:")
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print()

try:
    print(slice_me(family1, 0, -2))
except Exception as e:
    print("Error:", e)
print()

# Test case 2: Slicing out of bounds
print("Test case 2:")
try:
    print(slice_me(family, 0, 5))  # End index out of bounds
except Exception as e:
    print("Error:", e)
try:
    print(slice_me(family, -1, 2))  # Start index out of bounds
except Exception as e:
    print("Error:", e)
try:
    print(slice_me(family, 2, 1))  # Start index greater than end index
except Exception as e:
    print("Error:", e)
print()

# Test case 3: Non-list input
print("Test case 3:")
try:
    print(slice_me("not a list", 0, 2))
except Exception as e:
    print("Error:", e)
print()

# Test case 4: Non-2D array input
print("Test case 4:")
try:
    print(slice_me([1, 2, 3], 0, 2))
except Exception as e:
    print("Error:", e)
print()
