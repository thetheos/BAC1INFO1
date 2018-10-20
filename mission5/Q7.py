def sort_courses(student_courses):
  """
     pre: student_courses une liste de tuples (student, course)
     post: une liste triée de tuples (course, student)
  """
  courses_students = []
  for student, course in student_courses:
    courses_students.append((course, student))
  return sorted(courses_students)

def course_list(student_courses):
    l = []
    name = None
    for course, student in sort_courses(student_courses):
        if course != name:         # Condition course != name
            l.append(course)
            name = course
    return l

def nest_students(student_courses):
    matrix = []
    for i in course_list(student_courses):
        new_l = []
        for t in student_courses:
            if t[1] == i:
                new_l.append(t[0])
        matrix.append((i, new_l))
    return matrix


student_courses = [ ( "Jean", "LINFO1111" ), ( "Jean", "LINFO1101"), ( "Pierre", "LINFO1101" ), ( "Pierre", "LINFO1112" ) ]


print(nest_students(student_courses))

