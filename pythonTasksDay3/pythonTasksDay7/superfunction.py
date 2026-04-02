class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
    def student_greet(self) :
      print("hi student" +" "+ self.dept)


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def faculty_greet(self) :
       print("hi Teacher"+" "+ self.salary)

        

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
    def tempFaculty_greet(self) :
       print("hello")
