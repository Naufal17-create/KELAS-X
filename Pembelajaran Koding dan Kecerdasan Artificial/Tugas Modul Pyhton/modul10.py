# contoh 1
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


printme("hello world")


#contoh 2 penjumlahan sebuah barisan angka
def jumlah(angka):
    total = 0
    for x in angka:
        total += x
    return total

print("jumlah: ",jumlah((8,3,1,4,5)))


#contoh 3 pengecekan angka apakah ganjil atau genap?
def cek_ganjil_genap(angka):
    if angka%2==0:
        print("genap")
    else:
        print("ganjil")
    return

cek_ganjil_genap(5) #input angka, misalkan 5

#contoh 4 perhitungan rata - rata
def rata_rata(a,b,c):
    return (a+b+c)/3
rata_rata(1,2,3)
2.0

#contoh 5 perhitungan sederhana matematika
def kalkulator(angka1,angka2):
    print(angka1+angka2)
    print(angka1-angka2)
    print(angka1*angka2)
    print(angka1/angka2)    
    
kalkulator(1,2) #inputan 2 angka, angka1:1, dan angka2:2

#latihan
#1: Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter
#-notebook, jupyter-lab atau google colab
#2: Buatlah program menggunakan function dengan skenario sebagai berikut:
#a: Program menampilkan nilai faktorial dari angka yang di input, seperti pada contoh di bawah berikut:
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan angka: "))
hasil = faktorial(angka)
print("Faktorial dari", angka, "adalah", hasil)

#b: Program menampilkan karakter dari string upper case dan lower case pada sebuah string, untuk output diperlihatkan di bawah:
def karakter(string):
    print("Original String:", string)
    print("Lowercase:", string.lower())
    print("Uppercase:", string.upper())
    return
input_string = input("Masukkan string: ")
print("Original string:", input_string)
print("Jumlah karakter uppercase pada string: ", sum(1 for c in input_string if c.isupper()))
print("Jumlah karakter lowercase pada string: ", sum(1 for c in input_string if c.islower()))

#c: Program yang menampilkan segitiga pascal dari input angka, untuk outputnya dapat di lihat di video berikut:
n = int(input("input angka: "))

pascal = []

for i in range(n):
    row = [1] * (i + 1)
    
    # hitung isi tengah
    for j in range(1, i):
        row[j] = pascal[i-1][j-1] + pascal[i-1][j]
    
    pascal.append(row)

# cetak hasil
for r in pascal:
    print(r)


#d: Program yang menampilkan list angka yang di kali-kan dengan angka itu sendiri, untuk outputnya dapat di lihat di video berikut:
awal = int(input("awal range: "))
akhir = int(input("akhir angka sebelum = "))

hasil = []

for i in range(awal, akhir):
    hasil.append(i * i)

print(hasil)