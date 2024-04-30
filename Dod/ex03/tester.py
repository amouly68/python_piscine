from new_student import Student


try:
    student = Student(name="Edward", surname="agle")
    print(student)
    print(student.__dict__)
except Exception as e:
    print(e)

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
    print(student.__dict__)
except Exception as e:
    print(e)
