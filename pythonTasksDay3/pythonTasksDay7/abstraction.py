from abc import ABC, abstractmethod


class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass

    def login(self):
        print("User login successful")


class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def get_details(self):
        print("Student:", self.name, self.id, self.dept, self.fees)

    def login(self):
        print("Student login:", self.name)


class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        print("Faculty:", self.name, self.id, self.salary)

    def login(self):
        print("Faculty login:", self.name)