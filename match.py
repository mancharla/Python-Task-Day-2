#1 day number to day name using match case
day=int(input("enter the day number: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

#2 take  3 number
num1 = int(input("Enter a number: "))
match num1:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid number")

#3 Take four numbers
num2 =int(input("Enter a number: "))
match num2:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid number")