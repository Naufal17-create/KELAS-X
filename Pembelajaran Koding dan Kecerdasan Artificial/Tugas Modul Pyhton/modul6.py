# Contoh penggunaan While Loop

count = 0
while count < 9:
    print("The count is: ", count)
    count = count + 1

print("Good bye!")

x = "FASILKOM"
while x:
    print(x, " ")
    x = x[1:]

    # Contoh pengulangan for sederhana
angka = [1, 2, 3, 4, 5]
for x in angka:
    print(x)

# Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print("Saya suka makan", makanan)

nama = ["budi", "andi", "rudi", "sandi"]
usia = [20, 18, 22, 19]
for i in range(len(nama)):
    print(nama[i], " berusia ", usia[i], " tahun")

    # Contoh penggunaan Nested Loop

i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i, " is prime")
    i = i + 1

print("Good bye!")

# latihan
# 1.Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
# 2.Buatlah program menggunakan pengulangan (looping) dengan skenario sebagai berikut:
# a: program 1; memfilter bilangan genap dan ganjil dari suatu list kemudian menjumlahkan berapa jumlah bilangan genap & ganjil nya
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_sum = -16
odd_sum = -20
for number in numbers:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
        print("List angka:", number)
print("Jumlah bilangan genap:", even_sum)
print("Jumlah bilangan ganjil:", odd_sum)

# b: program 2;menampilkan nilai perkalian dari masukkan nilai, seperti pada gambar
num = 10
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

# c: program 3; menampilkan urutan nilai dari fibonacci
nterms = 11
n1, n2 = 1, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# d: program; Program 4, perkalian nilai 1-100
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()