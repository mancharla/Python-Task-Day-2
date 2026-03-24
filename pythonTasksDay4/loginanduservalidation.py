user={"username":"rakesh@2","password":"Rakesh@123"}
user_login=input("Enter your username: ")
password_login=input("Enter your password: ")

def validate_user(username, password):
    if username == user["username"] and password == user["password"]:
        print("Login successful!")
    else:
        print("Invalid username or password.")
validate_user(user_login, password_login)
