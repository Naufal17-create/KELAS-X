# (eps 14 : Classes part 2)


# Contoh class 2
class Animal: # parent class
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def greet(self):
        print("Hello!")

class Cat(Animal): # child class
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight

class Dog(Animal): # child class
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type


# Contoh class 1
class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def greet(self):
        print("Halo, " + self.name + "!")

p1 = Person("Cecep", 20, 95)
p2 = Person("Budi", 20, 80)

print(p1.__dict__)
print(p2.__dict__)

p1.greet()
p2.greet()