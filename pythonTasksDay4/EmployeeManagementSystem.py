user_list = []
user = {
    "name": "praveen kumar",
    "age": 30,
    "role": "software engineer",
    "salary": 50000
}
user_list.append(user)

user1 = {
    "name": "suresh kumar",
    "age": 28,
    "role": "data analyst",
    "salary": 45000
}
user_list.append(user1)

print("Employee List:")
print(user_list)

user_list[0]["salary"] = 60000
user_list[0]["role"] = "senior software engineer"

print("After Update:")
print(user_list)

user_list.pop(1)

print("After Delete:")
print(user_list)
