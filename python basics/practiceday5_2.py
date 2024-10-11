#highest score
student_scores = [190,180,124,134,156,178,167,145,150,190,199,179,180,123,145]
print(max(student_scores))
max_score = 0
for score in student_scores:
    if score>max_score:
        max_score = score 
print(max_score)        

