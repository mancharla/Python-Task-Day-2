def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average
nums = []
while True:
    value = input("Enter number : ")

    if value == "stop":
        break
    nums.append(int(value))

result = calculate_total(*nums)

print("Total :", result[0])
print("Average :", result[1])