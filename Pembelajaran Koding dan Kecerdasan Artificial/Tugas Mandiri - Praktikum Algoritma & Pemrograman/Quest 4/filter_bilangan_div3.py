list1 = [13, 15, 30, 41, 45, 55, 75, 95, 102, 135, 139, 151, 193, 200]

for angka in list1:
    if angka > 151:
        continue
    if angka % 3 == 0:
        print(angka)
