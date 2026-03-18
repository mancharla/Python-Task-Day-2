# 1 loop numbers
num=""
for i in range(1,50):
    num=num+str(i)+" "
print(num)

#2 even numbers
num =""
for i in range(1,100):
    if i%2==0:
        num=num+str(i)+" "
print(num)

#3 odd numbers
num =""
for i in range(1,100):
    if i%2!=0:
        num=num+str(i)+" "
print(num)

#4 mutiplication table 7
num=7
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#5 sum of first 1 to 100 numbers
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

#6 reverse of a number from 50 to 1
num=""
for i in range(50,0,-1):
    num=num+str(i)+""
print(num)

#7 divisible by 3 1-100 between count

count = 0
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
        count += 1
print("\nCount =", count)

#8 square of numbers 1-10
for i in range(1,11):
    print("square of",i,"is",i*i)

#9 cube of numbers 1-10
for i in range(1,11):
    print("cube of",i,"is",i*i*i)

#10 1-n numbers
n=int(input("enter a number: "))
for i in range(1,n+1):
    print(i,end=" ")

    