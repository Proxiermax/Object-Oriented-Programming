def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score

def calc_average_score(result):
    averages = {student: "{:.2f}".format(sum(scores.values()) / len(scores)) for student, scores in result.items()}
    # for student, scores in result.items():
    #     average_score = sum(scores.values()) / len(scores)
    #     averages[student] = average_score
    return averages
        
subject_score = {}
while True:
    student = input("input student id [0 to exit]:")
    if student == '0':
        print(result)
        average = calc_average_score(result)
        print("average :", average)
        break
    subject = input(f"input {student} subject :")
    score = int(input(f"input score of {subject} :"))
    result = add_score(subject_score, student, subject, score)
    print(result)