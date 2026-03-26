n = int(input("Enter a number: "))
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    elif n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(n))