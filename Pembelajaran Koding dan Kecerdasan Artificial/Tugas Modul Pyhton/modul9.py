#Contoh sederhana pembuatan tuple pada bahasa pemrograman python

tup1 = ('sistem komputer', 'teknik informatika', 2008, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

print(tup1)
print(tup2)
print(tup3)

#Cara mengakses nilai tuple

tup1 = ('sistem komputer', 'teknik informatika', 2008, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tup1[0] = 100;

# Jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print (tup3)

tup4= ('fisika', 'kimia', 1993, 2017)

#contoh penggunaan tuple
#program 1
#Create a tuple with different data types
print("program 1")
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#program 2
print("program 2")
#Create a tuple with numbers
tuplex = 5, 10, 15, 20, 25
print(tuplex)
#Create a tuple of one item
tuplex = 5,
print(tuplex)

print("program 3")
#program 3
#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

print("program 4")
#program 4
#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)


#Contoh cara membuat Dictionary pada Python

dict = {'Name': 'Luffy', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


#Update dictionary python

dict = {'Name': 'Luffy', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Mengubah entri yang sudah ada
dict['School'] = "Marijoa School" # Menambah entri baru

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#Contoh cara menghapus pada Dictionary Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # hapus entri dengan key 'Name'
dict.clear()     # hapus semua entri di dict
del dict         # hapus dictionary yang sudah ada

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


#contoh penggunaan dictionary

print("\ncontoh 1")
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

print("\ncontoh 2")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
cek_angka = 3
if cek_angka in d:
    print(cek_angka,' tersedia dalam dictionary')
else:
    print(cek_angka,'tidak tersedia dalam dictionary')

print("\ncontoh 3")
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

#latihan
#1: Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
#2: Buatlah program menggunakan list, dan materi sebelumnya dengan skenario sebagai berikut:
#a: Program yang menampilkan isi dari sebuah tuple kemudian mengkonversikan ke format string, untuk keluarannya dapat di lihat pada gambar di bawah:a
tuplex = ('g', 'a', 'n', 't', 'e', 'n', 'g')
str1 = ''.join(tuplex)
print("Isi dari tuple:", tuplex)
print(str1)

#b. Program yang menampilkan penjumlahkan bilangan yang ada pada dictionary, untuk keluarannya dapat di lihat pada gambar di bawah: 
dict = {'bilangan_1': 88, 'bilangan_2': -54, 'bilangan_3': 0.4}
total = sum(dict.values())
print("Dictionary:", dict)
print("Total penjumlahan bilangan pada dictionary:", total)

#c. Program yang menampilkan hasil perkalian dari setiap dictionary yang ada, untuk keluarannya dapat di lihat pada video di bawah: \
n = int(input("Masukkan angka: "))

hasil = {}  # dictionary kosong

for i in range(1, n + 1):
    hasil[i] = i * i   # atau i * n kalau mau dikali angka lain

print(hasil)

#d: Program yang menghapus key pada sebuah dictionary kemudian menampilkan perbedaan antara dictionary pertama kemudian yang sudah berubah, untuk keluarannya dapat di lihat pada video di bawah:
dict = {'a': 1, 'B': 2, 'C': 3, 'd': 4}
print("Dictionary sebelum dihapus:", dict)
del dict['a']
print("Dictionary setelah dihapus:", dict)

#e: Program permainan tebak nama binatang dalam bahasa inggris ke bahasa indonesia, untuk keluarannya dapat di lihat pada video di bawah:
# Dictionary hewan Inggris -> Indonesia
animals = {
    "Ant": "Semut",
    "Bee": "Lebah",
    "Mosquito": "Nyamuk",
    "Butterfly": "Kupu-kupu",
    "Spider": "Laba-laba",
    "Fly": "Lalat",
    "Hedgehog": "Landak",
    "Snail": "Siput"
}

print("Game Tebak Binatang dalam bahasa inggris\n")

play = input("Bermain ? (y untuk bermain)-> ")

if play.lower() == "y":
    for eng, indo in animals.items():
        print("\n" + eng)
        answer = input("Jawaban anda : ")

        # Normalize biar aman (huruf besar kecil / spasi / strip)
        normalize = answer.replace(" ", "").replace("-", "").lower()
        true_value = indo.replace(" ", "").replace("-", "").lower()

        if normalize == true_value:
            print("BENAR")
        else:
            print("SALAH")
            print("Jawaban yang dicari :", indo)
        print("------------------------------------")
else:
    print("Okay tidak bermain.")