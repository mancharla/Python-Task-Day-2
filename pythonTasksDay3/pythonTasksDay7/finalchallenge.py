from abc import ABC, abstractmethod
from functools import reduce
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
class Student(AbstractUser):
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees
    def get_details(self):
        print("Student:", self.name, self.fees)
class Faculty(AbstractUser):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        print("Faculty:", self.name, self.salary)
students = [
    Student("Rakesh", 40000),
    Student("Vikas", 70000),
    Student("Sandhya", 60000)
]
faculty = [
    Faculty("Anil", 25000),
    Faculty("Madhu", 50000),
    Faculty("Suresh", 45000)
]
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)
print("---- Sorted Students ----")
for s in students:
    print(s.name, s.fees)
print("---- Sorted Faculty ----")
for f in faculty:
    print(f.name, f.salary)
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("---- Filtered Students ----")
for s in high_fee_students:
    print(s.name, s.fees)

print("---- Filtered Faculty ----")
for f in high_salary_faculty:
    print(f.name, f.salary)

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees:", total_fees)
print("Total Salary:", total_salary)