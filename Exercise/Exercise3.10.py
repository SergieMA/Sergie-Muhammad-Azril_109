Favorit = ["Mie Ayam", "Ayam Teriyaki", "Bahasa Jawa", "Gunung Merbabu"]

# Mengakses elemen list
print(Favorit[0])

# Mengubah elemen list
Favorit[1] = "Ayam Bakar"  
print(Favorit[1])

# Menambahkan elemen baru ke list
Favorit.append("Nasi Goreng")   
print(Favorit)

# Menghapus elemen dari list
del Favorit[2]  
print(Favorit)

# Menghapus elemen terakhir menggunakan pop
Favorit.pop()
print(Favorit)

# Menghapus elemen berdasarkan posisi menggunakan pop
Favorit.pop(1)
print(Favorit)

# Menghapus elemen berdasarkan nilai
Favorit.remove("Mie Ayam")
print(Favorit)

# Karena tersisa 1 kita append terlebih dahulu
Favorit.append("Kerupuk")
Favorit.append("Fore")
print(Favorit)

# Mengurutkan sementara secara alfabetis
print(sorted(Favorit))

# Mengurutkan sementara secara alfabetis terbalik
print(sorted(Favorit, reverse=True))

# Membalik urutan list
Favorit.reverse()
print(Favorit)

# Mengembalikan urutan list
Favorit.reverse()
print(Favorit)

# Mengurutkan list secara alfabetis
Favorit.sort()
print(Favorit)

# Mengurutkan list secara alfabetis terbalik
Favorit.sort(reverse=True)
print(Favorit)

# Menghitung jumlah elemen dalam list
print(len(Favorit))
