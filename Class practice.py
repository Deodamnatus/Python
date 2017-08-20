students = []


class Student:

    school_name = "Bishop's"

    #dont pass self
    def __init__(self, name, student_id=0):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    #can overwrite attributes and methods
    school_name = "Bishop's Upper School"

    def get_name_capitalize(self):
        #use super to reference origonal class methods and attributes(Student)
        origonal_value = super().get_name_capitalize()
        return origonal_value + "-HS"

james = HighSchoolStudent("james", 11)

print(james.get_name_capitalize())

#mark = Student('Mark', 333)
#print(mark, Student.school_name)

