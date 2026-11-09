with open("Guest.txt", "w") as file:
    while True:
        name = input("Masukkan nama kamu (ketik 'q' untuk berhenti): ")

        if name == "q":
            break

        file.write(name + "\n")