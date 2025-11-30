# ("eps 13 : Classes part 1")


# ("Materi : create a class")
class Angka:
    jumlah = 8

a = Angka()
print(a.jumlah)
b = Angka()
print(b.jumlah)


# ("Materi : __init__()")

class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

p1 = Person("Cecep", 20, 95)
p1 = Person("Budi", 20, 80)