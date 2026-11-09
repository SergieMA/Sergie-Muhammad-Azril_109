name = input("Masukkan nama kamu: ")

with open("Guest.txt", "w") as file:
    file.write(name)