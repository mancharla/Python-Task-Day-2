from superfunction import User,Student,Faculty,TempFaculty
s = Student("john", "1","cse","40000")
s.student_greet()
f=Faculty("Rakesh","2","4000000")
f.faculty_greet()
tf=TempFaculty("vikki","3","30000","20")
tf.tempFaculty_greet()