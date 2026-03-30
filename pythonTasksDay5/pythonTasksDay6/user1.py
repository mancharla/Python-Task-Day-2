class user:
    def register(self):
        print("register")
    def login(self):
        print("login")
class student(user):
    def student_greet(self):
        print("hello student")
class faculty(user):
    def faculty_greet(self):
        print("hello faculty")
class tempfaculty(faculty):
    def tempfaculty_greet(self):
        print("hello temp faculty")
