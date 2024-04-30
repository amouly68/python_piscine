from new_student import Student


try:
    student = Student(name = "Edward", surname = "agle")
    print(student)
except Exception as e:
    print (e)

student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)