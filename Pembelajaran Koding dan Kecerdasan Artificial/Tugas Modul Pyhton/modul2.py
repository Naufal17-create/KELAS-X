#tipe data Boolean
print(True)

#tipe data String
print("string dengan menggunakan tanda kutip dua")
print('ini string menggunakan tanda kutip satu')
#tipe data string dengan menjelaskan spesial karakter atau escape sequences
print('ini adalah tanda single quote (\')')
print("ini adalah tanda double quote (\")")
print("ini adalah tanda slash (\\)")
print("Algoritma\nPemrograman") #menggunakan \n
print("Algoritma\bPemrograman") #menggunakan \b
print("Algoritma\tPemrograman") #menggunakan \t
print("Algoritma\rPemrograman") #menggunakan \b

#tipe data Integer
print(20)

#tipe data Float
print(3.14)
print(.2)
print(4.2e-3)

#tipe data Binary
print(0b10)

#tipe data octal
print(0o10)

#tipe data Hexadecimal
print('tipe data heksa desimal',0x10)

#tipe data Complex
print(5j)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Budi", 'umur':20})
#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"nama":"Budi", 'umur':21} #proses inisialisasi variabel biodata
print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
type(biodata) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary

#latihan
# 1.Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
#2.Buatlah program menggunakan variable dan tipe data, dengan output seperti di bawah
print("Praktikum Algoritma dan Pemrograman 1 - Variable dan Tipe Data")

# Boolean
a = False
print(a)
print(type(a))

# String
b = "Ini adalah tulisan berupa String"
print(b)

# Integer
c = 100
print(c)

# Float
d = 0.001
print(d)

# Hexadecimal -> decimal
e = 0x01
print(f"bilangan desimal dari 0x01 adalah {e}")

# Binary -> decimal
f = 0b1010
print(f)

# Complex number
g = complex(2, 6)
print(type(g))
print(g)
print(type(g))

# List angka
h = [96, 97, 98, 99, 100]
print(h)

# List string
i = ["seratus", "dua ratus", "tiga ratus"]
print(i)

# Dictionary
j = {"nama": "Ani", "umur": 19}
print(j)

# String dengan single quote
k = "This string contains a single quote (') character."
print(k)


# boolean
narkoba = False
belajar = True
print(narkoba)
print(belajar)

#string_format.py
first_name = "Budi"
middle_name = "Sigma"
last_name = "Santoso"

sapa = f"Halo {first_name} {middle_name} {last_name}"
print(sapa)