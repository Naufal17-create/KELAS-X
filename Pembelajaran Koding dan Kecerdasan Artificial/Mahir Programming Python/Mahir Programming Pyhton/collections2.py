# (eps 10 : Collections Data Types part 2)


# ("Materi : tuple")

tupleExample = ('Python', 20, 3.8, True, 20)
print(tupleExample)
tupleExample[1] = 30
print(tupleExample[-2])


# ("Materi : Dictionary")

customer = {
    "nama": "Naufal",
    "umur": 16
}
customer["pekerjaan"] = "siswa programmer"
customer.pop("umur")

print(customer)
print(customer["nama"])
print(customer["umur"])


# ("Materi : set")

numbers1 = {1, 3, 5, 4, 10}
numbers2 = {3, 4, 10, 7, 8}

# {10, 3, 4}
intersect = numbers1.intersection(numbers2)
print(intersect)

# {1, 5, 7, 8}
sym_difference = numbers1.symmetric_difference(numbers2)
print(sym_difference)

# {1, 3, 4, 5, 7, 8, 10}
numbers_union = numbers1.union(numbers2)

# {1, 5}
difference1 = numbers1.difference(numbers2)
print(difference1)