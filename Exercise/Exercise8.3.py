def make_shirt(size, message):
    print(f"Kamu memesan kaus ukuran {size} dengan tulisan '{message}'.")

# Menggunakan positional arguments
make_shirt('L', 'semangat belajar')

# Menggunakan keyword arguments
make_shirt(size='M', message='Tetap semangat')