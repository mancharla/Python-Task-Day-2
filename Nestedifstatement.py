#1 job eliglibility
age=int(input("enter your age: "))
height=int(input("enter your height: "))
weight=int(input("enter your weight: "))
if age>=18:
    if height>=160:
        if weight>=60:
            print("you are selected for the job")
        else:
            print("you are not rejected for the job")
    else:
        print("you are not rejected for the job")
else:
    print("you are not rejected for the job")

#2 college admission
age=int(input("enter your age: "))
marks=int(input("enter your marks: "))
if age>=17:
    if marks>=60:
        print("your admission is selected for the college")
    else:
        print("your admission is not selected for the college")
else:
    print("your admission is not selected for the college")

#3 sports selection Team
age=int(input("enter your age: "))
height=int(input("enter your height: "))
weight=int(input("enter your weight: "))
if age>=16:
    if height>=150:
        if weight>=50:
            print("you are selected for the sports team")
        else:
            print("you are not selected for the sports team")
    else:
        print("you are not selected for the sports team")
else:
    print("you are not selected for the sports team")