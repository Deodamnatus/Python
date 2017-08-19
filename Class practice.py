students = []


class Student:
    #dont pass self
    def __init__(self, name, student_id=0):
        student = {"name": name, "student_id": student_id}
        students.append(student)
    def __str__(self):
        return "Student"

mark = Student('Mark', 333)

print(students, mark)

