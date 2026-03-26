def create_user(name,role,age):
    user={"name":name.title(),"role":role,"age":age}
    return user
users=[]
users.append(create_user("raki", 24, "Engineer"))
users.append(create_user("john doe", 28, "Manager"))
users.append(create_user("sita", 22, "Developer"))

for user in users:
    print(user)
