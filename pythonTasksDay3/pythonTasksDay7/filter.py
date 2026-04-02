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


high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


for s in high_fee_students:
    print(s.name, s.fees)

print("------")

for f in high_salary_faculty:
    print(f.name, f.salary)