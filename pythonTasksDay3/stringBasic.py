# 1 characters in string
str="Hello, World"
print(len(str))

#2 vowels in string
str="Hello, World"
vowels=0
for i in str:
    if i in "aeiouAEIOU":
        vowels+=1
print(vowels)

#3 consonants in string
str="HelloWorld"
consonants=0
for i in str:
    if i.isalpha() and i not in "aeiouAEIOU":
        consonants+=1
print(consonants)

#4 reverse of string

str="rakesh"
rev=""
for i in str:
    rev=i+rev
print(rev)

#5 check if string is palindrome

str="madam"
rev=""
for i in str:
    rev=i+rev   
if str==rev:
    print("palindrome")