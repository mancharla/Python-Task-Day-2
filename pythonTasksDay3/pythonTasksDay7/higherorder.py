fees = [40000, 60000, 70000]


def add_bonus(x):
    return x + 5000


def process_users(users, func):
    return list(map(func, users))


result = process_users(fees, add_bonus)

print(result)