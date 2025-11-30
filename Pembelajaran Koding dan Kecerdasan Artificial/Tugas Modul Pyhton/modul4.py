#OPERATOR ARITMATIKA
#Penjumlahan
print(13 + 2)
mangga = 7
pisang = 9
buah = mangga + pisang
print(buah)

#Pengurangan
hutang = 10000
bayar = 5000
sisaHutang = hutang - bayar
print("Sisa hutang Anda adalah ", sisaHutang)

#Perkalian
panjang = 15
lebar = 8
luas = panjang * lebar
print(luas)

#Pembagian
kue = 16
anak = 4
kuePerAnak = kue / anak
print("Setiap anak akan mendapatkan bagian kue sebanyak ", kuePerAnak)

#Sisa Bagi / Modulus
bilangan1 = 14
bilangan2 = 5
hasil = bilangan1 % bilangan2
print("Sisa bagi dari bilangan ", bilangan1, " dan ", bilangan2, " adalah ", hasil)

#Pangkat
bilangan3 = 8
bilangan4 = 2
hasilPangkat = bilangan3 ** bilangan4
print(hasilPangkat)

#Pembagian Bulat
print(10//3) 
#10 dibagi 3 adalah 3.3333. Karena dibulatkan maka akan menghasilkan nilai 3

#latihan
#1.Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
#2.Buatlah program menggunakan operator dan tipe data, dengan skenario sebagai berikut:

#program 1: perhitungan sederhana
BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100
RumusPengjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan = BilanganKetiga - BilanganKedua - BilanganPertama
RumusPerkalian = BilanganPertama * BilanganKedua
print("Hasil dari penjumlahan ", BilanganPertama, " + ", BilanganKedua, " + ", BilanganKetiga, " adalah ", RumusPengjumlahan)
print("Hasil dari pengurangan ", BilanganKetiga, " - ", BilanganKedua, " - ", BilanganPertama, " adalah ", RumusPengurangan)
print("Hasil dari perkalian ", BilanganPertama, " * ", BilanganKedua, " * ", BilanganKetiga, " adalah ", RumusPerkalian)

#program 2: menghitung luas bangun datar
# 1. Luas Persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi
# 2. Luas Persegi Panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp
# 3. Luas Segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5*alas_segitiga*tinggi_segitiga
# Lanjutkan untuk luas lingkaran, luas jajaran genjang dan trapesium
print("Luas Persegi dengan panjang sisi ", panjang_sisi, " adalah ", luas_persegi)
print("Luas Persegi Panjang dengan panjang ", panjang_pp, " dan lebar ", lebar_pp, " adalah ", luas_pp)
print("Luas Segitiga dengan alas ", alas_segitiga, " dan tinggi ", tinggi_segitiga, " adalah ", luas_segitiga)

# program 3, buatlah program nya dengan output seperti pada gambar di bawah, gunakan operator bitwise, dengan menentukan berapakah nilai variabel a, b dengan nilai output seperti pada gambar
a = 0
b = 0
print("a & b =", a & b)
a = 13
b = 9
print("a | b =", a | b)
a = 9
b = 5
print("~a =", ~a)
a = 8
b = 5
print("a ^ b =", a ^ b)