def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(result):
    # total_score = 0
    # for i, (subject, score) in enumerate(result.items(), 1):
    #     total_score += score
    #     print(i, "-", subject, "-", score)
    # average_score = total_score/ len(result)
    # return average_score
    average_score = sum(result.values()) / len(result)
    return "{:.2f}".format(average_score)

subject_score = {}
while True:
    subject = input("input subject [0 to exit]:")
    if subject == '0':
        print(result)
        average = calc_average_score(result)
        print("average :", average)
        break
    score = int(input(f"input score of {subject} :"))
    result = add_score(subject_score, subject, score)
    print(result)