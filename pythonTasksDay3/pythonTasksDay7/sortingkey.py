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
    Student("Vikas", 30000),
    Student("Sandhya", 35000)
]

faculty = [
    Faculty("Anil", 70000),
    Faculty("Madhu", 50000),
    Faculty("Suresh", 60000)
]


students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)


for s in students:
    print(s.name, s.fees)

print("------")

for f in faculty:
    print(f.name, f.salary)