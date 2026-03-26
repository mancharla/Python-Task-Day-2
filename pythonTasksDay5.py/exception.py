try:
    numerator=int(input("enter a numerator number "))
    denomerator=int(input("enter a denomerator number"))
    result=numerator/denomerator
    print(result)
except ZeroDivisionError:
    print("you cannot divide with zero")
except ValueError:
   print("give only integer")

finally :
    print("program completed")



