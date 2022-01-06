class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name)

    def roll(self):
        print(self.age, self.name)


dog = Dog('willie', 6)
print(dog.name)
print(dog.age)
dog.roll()
dog.sit()
