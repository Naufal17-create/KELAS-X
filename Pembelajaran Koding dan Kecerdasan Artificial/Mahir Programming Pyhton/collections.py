# (eps 9 : Collections Data Types part 1)

# append, insert
# remove, pop, del, clear
# list iteration
# check if an item exists in list
# methods: len, copy, concat (+ dan extend), index, sort, reverse

listExample = [42, 'Python', 3.85, 50]

listExample.insert(1, 'Data Science')
listExample.append('Javascript')
print(listExample)


# ("Materi : remove")

print(listExample)
listExample.remove('Python')
print(listExample)


# ("Materi : pop")

print(listExample)
listExample.pop()
print(listExample)


# ("Materi : del")

print(listExample)
del listExample[2]
print(listExample)


# ("Materi : clear")

print(listExample)
listExample.clear()
print(listExample)

# ("Materi : list iteration")

listExample = [40, 55, 20, 75, 80]

for item in listExample:
    if item % 2 == 0:
        print(item)


# ("Materi : check if an item exists in list")

listExample = [40, 55, 20, 75, 80]

if 40 in listExample:
    print("Terdapat angka 40 di dalam listExample")


# ("Materi : methods: len, copy, concat (+ dan extend), index, sort, reverse")

# Materi reverse
listExample = [40, 55, 20]
listExample.reverse()

# Materi sort
listExample = [40, 55, 20]
listExample.sort()

print(listExample)

# Materi index
listExample = [40, 55, 20]
print(listExample.index(55))

# Materi concat (+ dan extend)
listExample = [40, 55, 20]
listExample2 = [70, 100]
print(listExample+listExample2)
listExample.extend(listExample2)
print(listExample)

# Materi copy
listExample2 = listExample.copy()
listExample2[0] = 100
print(listExample)
print(listExample2)

# Materi len
length = len(listExample)