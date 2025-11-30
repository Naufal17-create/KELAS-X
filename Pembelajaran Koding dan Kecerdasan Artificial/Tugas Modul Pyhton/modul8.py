# Contoh sederhana pembuatan list pada bahasa pemrograman python
list1 = ["sistem komputer", "teknik informatika", 2008, 2020]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
print(list1)
print(list2)
print(list3)


# Cara mengakses nilai di dalam list Python

list1 = ["sistem komputer", "teknik informatika", 2008, 2020]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list = ["sistem komputer", "teknik informatika", 2008, 2020]
print("Nilai ada pada index 2 : ", list[2])

list[2] = 2001
print("Nilai baru ada pada index 2 : ", list[2])

# Contoh cara menghapus nilai pada list python

list = ["sistem komputer", "teknik informatika", 2008, 2020]

print(list)
del list[2]
print("Setelah dihapus nilai pada index 2 : ", list)
["sistem komputer", "teknik informatika", 2008, 2020]

# program contoh yang memanfaatkan list
num = [-1, 2, 53, 5, 50, 153, 91, 87]
genap = [x for x in num if x % 2 == 0]
print("list angka ", num)
print("angka genap pada list tersebut: ", genap)

# program contoh yang memanfaatkan list
num = [-1, 2, 53, 5, 50, 153, 91, 87]
ganjil = [x for x in num if x % 2 != 0]
print("\nlist angka ", num)
print("angka ganjil pada list tersebut: ", ganjil)

s = ["g", "a", "n", "t", "e", "n", "g"]  # list
str1 = "".join(s)  # menggabungkan list
print(str1)  # menampilkan str1

# latihan
# 1: Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
# 2: Buatlah program menggunakan list, dan materi sebelumnya dengan skenario sebagai berikut:
# a: Program yang menampilkan nilai maksimum dari sebuah list, untuk keluarannya dapat di lihat pada gambar di bawah:
list1 = [1, -2, -8, 8, 3]
max_value = max(list1)
min_value = min(list1)
print("Nilai dari list:", list1)
print("Nilai minimum dari list:", min_value)

# c: Program yang menampilkan kata yang tidak boleh lebih dari 4 huruf, untuk keluarannya dapat di lihat pada gambar di bawah:
list1 = ["saya", "belajar", "python", "karena", "seru"]
ori = " ".join(list1)
print("Original string: ", ori)

kata = [word for word in list1 if len(word) > 4]
if kata:
    print("Program memfilter kata yang lebih dari 4 huruf...")
    print("Kata yang lebih dari 4 huruf:", kata)

# d: Program yang menampilkan sebuah anggota baru di antara setiap anggota list, untuk keluarannya dapat di lihat pada gambar di bawah:
list1 = ["Rusa", "Kelinci", "Burung", "Ikan"]
print("Original list:", list1)
list2 = ['a'] * (len(list1) * 2 - 1)
list2[::2] = list1
print("Memasukkan huruf a di antara anggota list:", list2)

#e: Program decrypt dari program di modul 7 mengenai enkripsi menggunakan caesar cipher, untuk keluarannya dapat di lihat pada gambar di bawah:
# Program decrypt Caesar Cipher

text = input("string yang dienkripsi: ")
shift = int(input("masukkan berapa langkah: "))

hasil = ""

for char in text:
    if char.isalpha():
        kode = ord(char) - shift

        if char.islower():
            if kode < ord('a'):
                kode += 26

        elif char.isupper():
            if kode < ord('A'):
                kode += 26

        hasil += chr(kode)
    else:
        hasil += char

print("pesan yang di dekrip:", hasil)