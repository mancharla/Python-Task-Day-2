def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


result = square_generator(5)
print(type(result))


for value in result:
    print(value)
def square_list(n):
    result = []
    for i in range(1, n+1):
        result.append(i*i)
    return result
a = square_list(5)
print(a)
print(type(a))