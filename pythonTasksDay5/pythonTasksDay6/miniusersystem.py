class User:
    users_count = 0   

    def __init__(self, user_name, pwd):
        self.__user_name = user_name      
        self.__pwd = pwd                  
        User.users_count += 1

    def get_user(self):
        return self.__user_name

    def register(self):
        print("registered:", self.__user_name)
        return self

    def login(self):
        print("logined:", self.__user_name)
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self

s1 = Student("john", "1234")
s1.login().greet().register()
print("------")
f1 = Faculty("ravi", "5678")
f1.login().greet().register()
print("Total Users:", User.users_count)