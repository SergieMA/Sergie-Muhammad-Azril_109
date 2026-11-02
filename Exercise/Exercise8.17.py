# City Names
def city_country(kota, negara):
    """Mengembalikan nama kota dan negara."""
    return f"{kota}, {negara}"


print(city_country('Jakarta', 'Indonesia'))
print(city_country('Tokyo', 'Jepang'))
print(city_country('Santiago', 'Chile'))

# Album 
def make_album(artis, judul_album, jumlah_lagu=None):
    """Membuat dictionary yang berisi informasi album."""
    album = {
        'artis': artis,
        'judul_album': judul_album
    }

    if jumlah_lagu is not None:
        album['jumlah_lagu'] = jumlah_lagu

    return album


album_1 = make_album('Noah', 'Bintang di Surga')
album_2 = make_album('Sheila On 7', '07 Des')
album_3 = make_album('Dewa 19', 'Bintang Lima')
album_4 = make_album('Peterpan', 'Alexandria', 10)

print(album_1)
print(album_2)
print(album_3)
print(album_4)

# Sandwiches
def buat_sandwich(*bahan):
    """Menampilkan daftar bahan sandwich yang dipesan."""
    print("\nSandwich yang dipesan:")

    for isi in bahan:
        print(f"- {isi}")


buat_sandwich('keju', 'telur')

buat_sandwich('daging sapi', 'saus', 'tomat')

buat_sandwich('ayam', 'keju', 'mayones', 'selada')