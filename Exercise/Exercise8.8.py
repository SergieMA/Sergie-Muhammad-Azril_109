def make_album(artis, judul_album, jumlah_lagu=None):
    album = {
        'artis': artis,
        'judul_album': judul_album
    }

    if jumlah_lagu is not None:
        album['jumlah_lagu'] = jumlah_lagu

    return album


while True:
    print("\nMasukkan informasi album.")

    artis = input("Masukkan nama artis (ketik 'q' untuk berhenti): ")

    if artis == 'q':
        break

    judul_album = input("Masukkan judul album: ")

    hasil_album = make_album(artis, judul_album)

    print(hasil_album)

print("\nProgram selesai.")