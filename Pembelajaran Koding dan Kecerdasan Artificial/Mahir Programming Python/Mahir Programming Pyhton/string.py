# (eps 5 : String)

# print("Selamat Datang di \"coding studio\"!")

# ("Materi : String Method")
text = 'Belajar Python'

print(text.upper())
print(text.split(' '))
print(text.index('a'))

# ("Materi : Slicing String")

print(text[0])
print(text[:5])

# ("Materi : String Concatenation")

mangga = 5
pisang = 7
apel = 4
text = "Cecep membeli {} mangga, {} apel, dan {} pisang."
print(text.format(mangga, apel, pisang))

# ("Materi : String Format")

text = "Saya senang belajar Python."
print("Python" in text)
print("Javascript" in text)