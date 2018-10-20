"""
le code intervertie les couples student-course puis le trie par ordre alphabetique:
Retirer course != name reviendrait a rajouter plusieurs fois le mpeme cours dans la liste


"""

def sort_courses(student_courses):
  """
     pre: student_courses une liste de tuples (student, course)
     post: une liste triée de tuples (course, student)
  """
  courses_students = []
  for student, course in student_courses:
    courses_students.append((course, student))
  return sorted(courses_students)

student_courses = [ ( "Jean", "LINFO1111" ), ( "Jean", "LINFO1101"), ( "Pierre", "LINFO1101" ), ( "Pierre", "LINFO1112" ) ]

l = []
name = None
for course, student in sort_courses(student_courses):
   if course != name:         # Condition course != name
      l.append(course)
      name = course

print ( l )