#전공평점 = (학점 x 과목평점)의 합 / 학점의 총합 
dict = { 'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0
}

sum_grade = 0
tmp = []
result = 0
for _ in range(20):
    course, grade, course_grade = input().split()
    if course_grade in dict:
        tmp.append(float(grade)*dict[course_grade])
        sum_grade += float(grade)

result = sum(tmp)/sum_grade
print(result)