print("Hello World")
#Untuk mengakses substring, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan substring Anda. Sebagai contoh :
name = 'John Doe'
message = "John Doe belajar bahasa python di Belajarpython"
print ("name[0]: ", name[0])
print ("message[1:4]: ", message[1:4])
#mengupdate string
message = 'Hello World'
print ("Updated String :- ", message[:6] + 'Python')


kutipantiga = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print (kutipantiga)

#latihan
#1: Jalankan program di atas di komputer anda, menggunakan pycharm, jupyter-notebook, jupyter-lab atau google colab
#2: Buatlah program menggunakan numbers dan string:
#a: String arrays, misalkan terdapat string a = "Hello World" yang ingin di tampilkan adalah index ke-2,4,8,10 secara terpisah ingat: indexing dimulai dari 0
a = "Hello World"
print("Index ke-2:", a[2])
print("Index ke-4:", a[4])
print("Index ke-8:", a[8])
print("Index ke-10:", a[10])
#b: String range (slicing), misalkan terdapat string a = "Hello World" yang ingin di tampilkan pada output di bawah
a = "Hello World"
print("Index ke-0 sampai ke-4:", a[1:3])
print("Index ke-5 sampai ke-9:", a[2:5])
print("Index ke-10 sampai ke-14:", a[6:10])

#c: fungsi lowercase, uppercase dan replace, misalkan terdapat string a = "Hello World" yang ingin di tampilkan pada output di bawah yaitu mengubah string menjadi huruf kecil(lowercase) dan kapital(uppercase), serta menggantikan salah satu karakter menjadi karakter lain
a = "Hello World"
b = "Selamat pagi dan selamat sore dan selamat siang dan selamat malam"
print("Original String:", a)
print("Lowercase:", a.lower())
print("Uppercase:", a.upper())
print("Original String:", b)
print("Replace String a,o,e menjadi i", b.replace("a", "i").replace("o", "i").replace("e", "i"))

#d: implementasikan sebuah enkripsi caesar cipher, yang bisa anda baca di Caesar cipher, untuk outputnya dapat anda lihat di bawah:
def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Masukkan string: ")
langkah = input("Masukkan berapa langkah: ")
shift = int(langkah) % 26
encrypted_text = caesar_cipher(text, shift)
print("Original String:", text)
print("Hasil enkripsi:", encrypted_text)