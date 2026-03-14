#1 last digit of a number
a=input("enter a number: ")
print(a[len(a)-1])

#2 unit digit using % operator
b=int(input("enter a number: "))
print(b%10)

#3 last digit using // operator
c=int(input("enter a number: "))
print(c//10)

#4 second last digit
d=int(input("enter a number: "))
print(d//10%10)

#5 five digit number
a1="10001"
print(a1[len(a1)-1])