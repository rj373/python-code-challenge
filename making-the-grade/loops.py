"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [round(item) for item in student_scores]
    
def count_failed_students(student_scores):
    count_f=0
    for item in student_scores:
        if item<=40:
            count_f+=1
        else:
            pass
    return count_f
    
def above_threshold(student_scores, threshold):
    count_t=[]
    for item in student_scores:
        if item>=threshold:
            count_t.append(item)
        else:
            pass
    return count_t
    
def letter_grades(highest):
    interval=round((highest-41)/4)
    return [*range(41,highest,interval)]
    
def student_ranking(student_scores, student_names):
    ranking = []
    for i in range(len(student_scores)):
        ranking.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return ranking
    
def perfect_score(student_info):
    found=[]
    for student in student_info:
        if student[1]==100:
            found=student
            break
    return found