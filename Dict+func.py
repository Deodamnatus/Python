#Student list, gpa and password organizer



#get unique student id
def student_get_id():
    try:
        # try to open id_storage.txt and assign contents to current_id
        with open("id_storage.txt", "r") as current_id_file:
            current_id = int(current_id_file.read())
    except FileNotFoundError:
        # if file doesn't exist, set make file and reset current_id
        current_id = 0
        current_id_file = open("id_storage.txt", "w")
        current_id_file.write(str(0))
        current_id_file.close()
    # write current_id + 1 to file
    with open("id_storage.txt", "w") as current_id_file:
        current_id_file.write(str(current_id + 1))
    # return current_id in 5 digit format
    return '{:05d}'.format(current_id)

#add student to list as dictionary
def add_student(name, GPA, password, list):
    student_dictionary = { "Name" : name, "GPA" : GPA, "Password" : password, "id" : student_get_id()}


    # update text file based on new student
    def update_list_file(student_dictionary):
        with open("student_dictionaries.txt", "a") as student_dictionaries_file:
            student_dictionaries_file.write(str(student_dictionary) + "\n")  # import list of dictionaries

    update_list_file(student_dictionary)
    list.append(student_dictionary)

    #creates dictionary student_$student_id and appends it to list and list file
    #exec("student_" + str(student_id) + ' = {"Name" : "' + str(name) + '", "GPA" : ' + str(GPA) + ', "Password" : "' + str(password) + '", "id" : ' + str(student_id) + '}')




student_dictionaries=[]
# tries to open student_dictionaries.txt and assign student_dictionaries to list in file. otherwise creates new list
try:
    with open("student_dictionaries.txt", "r") as student_dictionaries_file:
        for line in student_dictionaries_file.readlines():
            student_dictionaries.append(line)
except FileNotFoundError:
    print("Creating data file...")


#add menu interface, options should be: add student(s), search students, remove student(s), add a new category like a test grade and assign it for each one. Could add spreadsheet import info for student info
continue_inputing = "y"
while continue_inputing == "y":
    student_name = input("Name: ")
    student_GPA = input("GPA: ")
    student_password = input("Password: ")
    add_student(name=student_name, GPA=student_GPA, password=student_password, list=student_dictionaries)
    continue_inputing = input("Would you like to continue adding students?(y/n): ")
    while continue_inputing != "y" and continue_inputing != "n":
        continue_inputing = input("Please format input as y/n: ")

print(student_dictionaries)

