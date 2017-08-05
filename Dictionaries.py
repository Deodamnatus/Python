student={
    "name": "Jeremy",
    "student_id": 15352,
    "GPA": 3.42,
    "feedback": None
}
all_students=[
    {"name":"Mark", "GPA": 3.42},
    {"name":"Jill", "GPA": 3.42},
]
print(student["GPA"])
print(student.get("student_id"))
print(student.get("lunch_schedule", "unknown"))
student["last_name"]="Gleeson"
try:
    last_name=student["last_name"]
    numbered_last_name= 3+ last_name
except KeyError:
    print("Error finding last name!!!")
except TypeError as error:
    print("I can't add these two together")
    print(error)
except Exception: #handles all excpetions
    print("unknown error")
#del student["GPA"]
print(student.keys())
print(student.values())
