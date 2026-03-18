#1 print 1-20 numbers
num=0
while num<20:
    num+=1
    print(num,end=" ")

#2 factorial of a number
num=int(input("enter a number: "))
factorial=1
while num>0:
    factorial=factorial*num
    num-=1
    print(factorial)
#3 reverse of a number
num=int(input("enter a number: "))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
print(rev)

#4 counts digits in a number
num=int(input("enter a number: "))
count=0
while num>0:
    num//=10
    count+=1
print(count)

#5 input until user stop
while True:
    text=input("enter something:")
    if text=="stop":
        break
print(text)