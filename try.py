class Fish():
    def __init__(self, age, length, isAlive):
        self.age = age
        self.length = length
        self.isAlive = isAlive


    def add_age(self, howmuch):
        self.age += howmuch
fishy1 = Fish(8, 50, True)
fishy1.add_age(6)
print(fishy1.age)