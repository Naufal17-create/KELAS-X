# Program menghitung jumlah Huruf & Angka

inputan = input("Inputan: ")

huruf = 0
angka = 0

for x in inputan:
    if x.isdigit():
        angka += 1
    elif x.isalpha():
        huruf += 1

print("Kata :", huruf)
print("Angka :", angka)