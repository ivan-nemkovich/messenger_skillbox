class User:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class AgedUser(User):
    __age: int

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        self.__age = age

    def full_name(self):
        return super().full_name() + f", {self.__age}"


aged_john = AgedUser("John", "Doe", 30)

print(aged_john.full_name())
