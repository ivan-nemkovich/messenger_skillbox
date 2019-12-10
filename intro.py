"""
age = input("Your age?: ")

if int(age) > 14:
    print("Access deny!")
elif int(age) >= 0:
    print("You are velcome!")

users = ["Artur", "John", "Jack"]
for user in users:
    print("Hello, " + user + "!")

counter = 0
while counter < 10:
    print(counter)
    counter +=1

users = ["Artur", "John", "Jack"]
more_users = ["Nic", "Jo", "Mary"]

def print_users(data):
    for a in data:
        print("Hello, " + a + "!")

print_users(more_users)
"""


class User:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


artur = User("Artur", "Doe")
john = User("John", "Doe")

print(john.full_name())
