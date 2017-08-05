#generator practice and syntax

#string generator thing: squares = (x*x for x in [1,2,3,4,5])
#string list thing     : squares = [x*x for x in [1,2,3,4,5])
#second change
students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except FileNotFoundError:
        print("File does not exist")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)


def read_list_test(list_of_students):
    for item in list_of_students:
        yield item


list_test = ["asdf", "ghjk", "kl;"]
for i in read_list_test(list_test):
    print(i)
