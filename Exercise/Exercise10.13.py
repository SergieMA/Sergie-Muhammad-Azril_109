import json

user = {}

user["nama"] = input("Masukkan nama: ")
user["umur"] = input("Masukkan umur: ")
user["kota"] = input("Masukkan kota: ")

with open("user.json", "w") as file:
    json.dump(user, file)

with open("user.json") as file:
    data = json.load(file)

print("\nInformasi yang saya ingat:")
print(f"Nama: {data['nama']}")
print(f"Umur: {data['umur']}")
print(f"Kota: {data['kota']}")