students = []


class Student:
    school_name = "norte"

    def __init__(self, name, student_id=332):
        self.name = name

        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def get_student_id(self):
        return self.student_id

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school(self):
        return self.school_name
