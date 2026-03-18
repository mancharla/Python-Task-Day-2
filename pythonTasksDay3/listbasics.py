#1 sum of list
list=[1, 2, 3, 4, 5]
sum=0
for i in list:
    sum+=i
print(sum)

#2 maximum in list
list=[1, 2, 3, 4, 5]
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)
 
#3 minimum in list
list=[1, 2, 3, 4, 5]
min=list[0]
for i in list:
    if i<min:
        min=i
print(min)

#4 to find the length of list

list=[1,2,3,4,5,6,7,8,9,10]
len=0
for i in list:
    len+=1
print(len)

#5 check elemnet exit in list or not

list=[1,2,3,4,5]
n=int(input("enter the number to check: "))
if n in list:
    print("number exist in list")
else:
    print("number does not exist in list")
