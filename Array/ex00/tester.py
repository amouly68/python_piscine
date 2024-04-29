from give_bmi import give_bmi, apply_limit

# Test case 1: Normal case
height1 = [2.71, 1.15]
weight1 = [165.3, 38.4]
print("Test case 1:")
print("Height:", height1)
print("Weight:", weight1)
bmi1 = give_bmi(height1, weight1)
print("BMI:", bmi1)
print("Above limit:", apply_limit(bmi1, 26))
print()

# Test case 2: Lists of unequal lengths
height2 = [2.71, 1.15, 1.8]
weight2 = [165.3, 38.4]
print("Test case 2:")
print("Height:", height2)
print("Weight:", weight2)
try:
    bmi2 = give_bmi(height2, weight2)
    print("BMI:", bmi2)
    print("Above limit:", apply_limit(bmi2, 26))
except Exception as e:
    print("Error:", e)


# Test case 3: Empty lists
height3 = []
weight3 = []
print("Test case 3:")
print("Height:", height3)
print("Weight:", weight3)
try:
    bmi3 = give_bmi(height3, weight3)
    print("BMI:", bmi3)
    print("Above limit:", apply_limit(bmi3, 26))
except Exception as e:
    print("Error:", e)


# Test case 4: Lists with characters
height4 = [2.71, 'abc', 1.8]
weight4 = ['def', 38.4, 60]
print("Test case 4:")
print("Height:", height4)
print("Weight:", weight4)
try:
    bmi4 = give_bmi(height4, weight4)
    print("BMI:", bmi4)
    print("Above limit:", apply_limit(bmi4, 26))
except Exception as e:
    print("Error:", e)
