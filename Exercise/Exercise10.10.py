filenames = ["Book1.txt", "Book2.txt"]

for filename in filenames:
    with open(filename, encoding="latin-1") as file:
        contents = file.read()

    jumlah = contents.lower().count("the")

    print(f"{filename}: {jumlah} kata 'the'")