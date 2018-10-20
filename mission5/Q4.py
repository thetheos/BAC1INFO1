def students(course, student_courses):
    student = []   
    for i in student_courses:
        if i[1] == course:
            student.append(i[0])
    return student

