# Program Permainan Gunting, Batu, Kertas

while True:
    print("Pemain 1: Silahkan anda pilih : Gunting, Batu, Kertas -> ", end="")
    p1 = input().lower()

    print("Pemain 2: Silahkan anda pilih : Gunting, Batu, Kertas -> ", end="")
    p2 = input().lower()

    # Menentukan pemenang
    if p1 == p2:
        print("Permainan Seri")
    elif (p1 == "gunting" and p2 == "kertas") or \
         (p1 == "batu" and p2 == "gunting") or \
         (p1 == "kertas" and p2 == "batu"):
        print("Pemain 1 Menang")
    else:
        print("Pemain 2 Menang")

    print("Apakah Anda Ingin memulai Permainan Awal lagi [Y/y] atau [Tidak/t] -> ", end="")
    ulang = input().lower()

    if ulang != 'y':
        print("GAME OVER")
        break

    print("Permainan Baru Akan dimulai")
    print()
