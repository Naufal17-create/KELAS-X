# Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE

nilai = 9

# jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
if nilai > 7:
    print("Selamat Anda Lulus")

# jika kondisi salah/FALSE maka program tidak akan mengeksekusi perintah dibawahnya
if nilai > 10:
    print("Selamat Anda Lulus")


# Kondisi if else adalah jika kondisi bernilai TRUE maka akan dieksekusi pada if, tetapi jika bernilai FALSE maka akan dieksekusi kode pada else

nilai = 3
# Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi, tetapi jika FALSE kode pada else yang akan dieksekusi.
if nilai > 7:
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")


# Contoh penggunaan kondisi elif

hari_ini = "Minggu"

if hari_ini == "Senin":
    print("Saya akan kuliah")
elif hari_ini == "Selasa":
    print("Saya akan kuliah")
elif hari_ini == "Rabu":
    print("Saya akan kuliah")
elif hari_ini == "Kamis":
    print("Saya akan kuliah")
elif hari_ini == "Jumat":
    print("Saya akan kuliah")
elif hari_ini == "Sabtu":
    print("Saya akan kuliah")
elif hari_ini == "Minggu":
    print("Saya akan libur")

# latihan
# 1.Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
# 2.Buatlah program menggunakan kondisi if, if else, dan elif dengan skenario sebagai
# a: program 1;  Program python untuk melakukan pengecekan apakah segitiga tersebut merupakan segitiga sama sisi (Equilateral Triangle), segitiga sama kaki (Isosceles triangle), atau segitiga sembarang (scalene triangle)
sisi1 = 12
sisi2 = 2
sisi3 = 12
if sisi1 == sisi2 and sisi2 == sisi3:
    print("Segitiga tersebut adalah segitiga sama sisi (Equilateral Triangle)")
elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
    print("Segitiga tersebut adalah segitiga sama kaki (Isosceles triangle)")
else:
    print("Segitiga tersebut adalah segitiga sembarang (scalene triangle)")

    # b: program 2;Program python untuk melakukan pengecekan apakah tahun yang kita inisialisasikan merupakan tahun kabisat atau tidak. berikut output program pengecekan tahun kabisat (tahun 2019,2020)

tahun = 2020
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print("Tahun:", tahun)
    print(tahun, "adalah tahun kabisat")
else:
    print("Tahun:", tahun)
    print(tahun, "bukan tahun kabisat")

# c: program 3; Program python untuk mendeteksi zodiak/astrologi yunani dari tanggal dan bulan lahir anda.
tanggal = 14
bulan = 5
if (tanggal >= 21 and bulan == 3) or (tanggal <= 19 and bulan == 4):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Aries")
elif (tanggal >= 20 and bulan == 4) or (tanggal <= 20 and bulan == 5):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Taurus")
elif (tanggal >= 21 and bulan == 5) or (tanggal <= 20 and bulan == 6):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Gemini")
elif (tanggal >= 21 and bulan == 6) or (tanggal <= 22 and bulan == 7):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Cancer")
elif (tanggal >= 23 and bulan == 7) or (tanggal <= 22 and bulan == 8):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Leo")
elif (tanggal >= 23 and bulan == 8) or (tanggal <= 22 and bulan == 9):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Virgo")
elif (tanggal >= 23 and bulan == 9) or (tanggal <= 22 and bulan == 10):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Libra")
elif (tanggal >= 23 and bulan == 10) or (tanggal <= 21 and bulan == 11):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Scorpio")
elif (tanggal >= 22 and bulan == 11) or (tanggal <= 21 and bulan == 12):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Sagittarius")
elif (tanggal >= 22 and bulan == 12) or (tanggal <= 19 and bulan == 1):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Capricorn")
elif (tanggal >= 20 and bulan == 1) or (tanggal <= 18 and bulan == 2):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Aquarius")
elif (tanggal >= 19 and bulan == 2) or (tanggal <= 20 and bulan == 3):
    print("tanggal anda lahir adalah:", tanggal)
    print("bulan anda lahir adalah:", bulan)
    print("Zodiak Anda adalah Pisces")

#d: program 4; Program python untuk mendeteksi zodiak/astrologi cina dari tahun lahir anda.
tahun = 2024
zodiak_cina = ["Tikus", "Kerbau", "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing", "Monyet", "Ayam", "Anjing", "Babi"]
index = (tahun - 4) % 12
print("Tahun:", tahun)
print("Zodiak Cina Anda adalah:", zodiak_cina[index])