students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id = "none"): #incase a student id is not supplied, 332 will be default
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")


def read_students(f):
    for line in f:
        yield line


read_file()
print_students_titlecase()

student_name = input("enter student name: ")
student_id = input("enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)




