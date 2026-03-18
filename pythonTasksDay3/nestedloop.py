# 1 pattern *
for i in range(1, 5):
        print("*"*i)

# 2 pattern number 
for i in range(1, 5):
        for j in range(1,1+i):
                print(j,end="")
        print()
        
# 3 pattern number multiplication tables (1to5)
for i in range(1, 6):
        for j in range(1, 11):
                print(i*j,end="\t")
        print()

#4 pattern 
for i in range(1,4):
        for j in range(1,2):
                print("A B C",end=" ")
        print()

#5 pattern 
num=1
for i in range(1,4):
        for j in range(1,4):
                print(num,end=" ")
                num=num+1
        print()