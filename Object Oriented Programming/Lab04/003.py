class Student:
    def __init__(self, student_id, student_name, student_mentor):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mentor = student_mentor
    
    def call_mentor(self):
        return self.student_mentor

student1 = Student("66010333", "Alice", "65010444")
student2 = Student("65010444", "Bulio", "64010555")
student3 = Student("64010555", "Clayn", "63010666")
student4 = Student("63010666", "Danum", None)

def call_student_mentor(id_tag):
    enrolled_students_names = []
    enrolled_students_id = []
    current_student = None
    for student in [student1, student2, student3, student4]:
        if student.student_id == id_tag:
            break
    try:
        while current_student.student_mentor is not None:
            mentor = None
            for student in [student1, student2, student3, student4]:
                if student.student_id == id_tag:
                    current_student = student
                    break
                # if student.student_id == current_student.student_mentor:
                #     mentor = student
                #     break
            if mentor:
                enrolled_students_names.append(mentor.student_name)
                enrolled_students_id.append(mentor.student_id)
                current_student = mentor
            else:
                break
    except: pass
    if len(enrolled_students_id) != 0:
        return [enrolled_students_names,enrolled_students_id]
    else:
        return "No mentor"
    
def check_mentor(id1, id2):
    return id1 in call_student_mentor(id2)[1] or id2 in call_student_mentor(id1)[1]

# Alice, Bulio, Clayn, Danum
# 66010333, 65010444, 64010555, 63010666

result1 = call_student_mentor("66010333")
print(result1)

result2 = check_mentor("64010555", "66010333")
print(result2)

    # check_flag = False
    # first_check = False
    # current_student = None
    # for student in [student1,0 student2, student3, student4]:
    #     if student.student_name == name1:
    #         current_student = student
    #         first_check = True
    #         break
    # if not first_check:
    #     return check_flag
    # while True:
    #     # print(current_student.student_mentor)
    #     mentor = None
    #     if current_student.student_name == name2:
    #         check_flag = True
    #         break
    #     for student in [student1, student2, student3, student4]:
    #         if student.student_name == current_student.student_mentor:
    #             mentor = student
    #             break
    #     if mentor:
    #         current_student = mentor
    #     else:
    #         break
    # return check_flag