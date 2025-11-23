# (eps 12 : Function part 2)


# ("Materi : lambda function")

# cara 1
def add5(number):
    total = number + 5
    return total

number = 10
number_added_5 = add5(number)
print(number_added_5)

# cara 2
number = 10
total = lambda n: n+5
print(total(number))