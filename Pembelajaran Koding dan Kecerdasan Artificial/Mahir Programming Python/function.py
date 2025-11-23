# (eps 11 : Function part 1)


# ("Materi : create and call")

def greet():
    print("Hello Stranger!")
    print("Nice to meet you.")

greet()
greet()


# ("Materi : passing arguments")

# Parameter = name, age
def greet(name, age):
    print("Name: " + name)
    print("Age: " + str(age))

Argument = "Budi", 20
greet("Budi", 20)
greet(age=20, name="Cecep")
greet(20, "Cecep")