#STARTER CODE — student_portal.py

def login_required(func):

    def wrapper(*args, **kwargs):

        print("Login Successful")

        return func(*args, **kwargs)

    return wrapper

def activity_logger(func):

    def wrapper(*args, **kwargs):

        print("Activity Logged")

        return func(*args, **kwargs)

    return wrapper

class Student: 

    def __init__(self, name, roll_no):

        self.name = name

        self.roll_no = roll_no
    @login_required
    @activity_logger
    def show_profile(self):

        print(f"{self.name} | {self.roll_no}")


def make_greeting(message):

    def greet(student):

        print(message + student.name)

    return greet

greet_Welcome = make_greeting("Welcome, ")
greet_morning = make_greeting("Good Morning, ")
s1 = Student("Rahul", 1)
s1.show_profile()
greet_Welcome(s1)
s2 = Student("Priya", 2)
s2.show_profile()
greet_morning(s2)



