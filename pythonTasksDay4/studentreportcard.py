student = {
    "name": "rakesh reddy",
    "maths": 85,
    "science": 78,
    "english": 90
}

def report():
    total = student["maths"] + student["science"] + student["english"]
    average = total / 3

    print("Student Report Card")
    print("Name :", student["name"])
    print("Maths :", student["maths"])
    print("Science :", student["science"])
    print("English :", student["english"])
    print("Total :", total)
    print("Average :", average)

    if average >= 90:
        print("Grade : A")
    elif average >= 75:
        print("Grade : B")
    elif average >= 60:
        print("Grade : C")
    else:
        print("Grade : Fail")

report()