from functools import reduce


class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


students = [
    Student("Rakesh", 40000),
    Student("Vikas", 60000),
    Student("Sandhya", 70000)
]

faculty = [
    Faculty("Anil", 25000),
    Faculty("Madhu", 50000),
    Faculty("Suresh", 45000)
]


total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)


print("Total Fees:", total_fees)
print("Total Salary:", total_salary)