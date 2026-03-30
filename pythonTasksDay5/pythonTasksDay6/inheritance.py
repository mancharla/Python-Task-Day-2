from user1 import user,student,faculty,tempfaculty


student1=student()
student1.student_greet()
faculty1=faculty()
faculty1.faculty_greet()
student1.register()
faculty1.login()

#user1=user()
#user1.user_greet() # not possible parent to child we cannot access

tempfaculty1=tempfaculty()
tempfaculty1.tempfaculty_greet()
tempfaculty1.faculty_greet()
tempfaculty1.register()

