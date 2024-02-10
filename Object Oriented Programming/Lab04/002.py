class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.students_list = []
        self.teacher_list = []
    def add_stu(self, stu):
        self.students_list.append(stu)
    def add_tch(self, tch):
        self.teacher_list.append(tch)
        
class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

student1 = Student("66010333", "Alice")
student2 = Student("66010444", "Minji")
student3 = Student("66010555", "Hanni")
student4 = Student("66010666", "Naeum")
student5 = Student("66010777", "Croew")
teacher1 = Teacher("99910880", "P.Smith")
teacher2 = Teacher("99910887", "P.Yoida")
oop_section1 = Subject("10248701", "OOP 1", "Sec A", 3)
oop_section2 = Subject("10248702", "OOP 2", "Sec B", 3)
oop_section1.add_stu(student1)
oop_section1.add_stu(student2)
oop_section1.add_stu(student3)
oop_section2.add_stu(student4)
oop_section2.add_stu(student5)
oop_section1.add_tch(teacher1)
oop_section2.add_tch(teacher2)

def call_students_from_teacher(teacher_id):
    enrolled_students = []
    for section in [oop_section1, oop_section2]:
        if teacher_id in section.teacher_list[0].teacher_id:
            for student in section.students_list:
                enrolled_students.append(student.student_name)
    return enrolled_students

def call_subject_from_student(student_id):
    enrolled_subjects = []
    for section in [oop_section1, oop_section2]:
        for student in section.students_list:
            if student.student_id == student_id:
                enrolled_subjects.append(section.subject_name)
    return enrolled_subjects

print(call_students_from_teacher("99910880"))
print(call_subject_from_student("66010333"))

# ("66010333", "Alice")
# ("66010444", "Minji")
# ("66010555", "Hanni")
# ("66010666", "Naeum")
# ("66010777", "Croew")
# ("99910880", "P.Smith")
# ("99910887", "P.Yoida")