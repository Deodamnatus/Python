#use def to define function
'''
def return1():
    return 1
def print2():
    print("2")

variable=return1()
print(variable)
print2()
variable=print2()
print(variable)
if not variable:
    print("variable not defined")
'''

def generate_student_id():
    # read file and increment 1 and use that as id
    id=222
    return id
def add_student(student_name="Jeremy", student_id=generate_student_id()):
    print(student_name)
    print(student_id)

def var_args(name, *arguments):
    print(name)
    print(arguments)
    #makes arguments into list

def key_word_args_args(name, **arguments):
    print(name)
    print(arguments)
    #makes arguments into list

key_word_args_args("Jeremy", id=221, Description="Student", GPA="3.22")
#var_args("Jeremy", 3, None, "happy")
#print_student(None, 221)