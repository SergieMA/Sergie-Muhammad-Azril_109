import json

favorite_number = input("Masukkan angka favorit kamu: ")

with open("favorite_number.json", "w") as file:
    json.dump(favorite_number, file)