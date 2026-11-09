filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(contents)

    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")