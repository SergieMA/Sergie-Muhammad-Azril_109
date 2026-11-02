person_1 = {
    "first_name": "Sergie",
    "last_name": "Azril",
    "age": 18,
    "city": "Karawang",
    "occupation": "Mahasiswa",
    "hobby": "Fotografi"
}

person_2 = {
    "first_name": "Windi",
    "last_name": "Aulia",
    "age": 19,
    "city": "Jakarta",
    "occupation": "Pelajar",
    "hobby": "Basket"
}

person_3 = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "age": 20,
    "city": "Bandung",
    "occupation": "Karyawan",
    "hobby": "Membaca"
}

people = [person_1, person_2, person_3]

for person in people:
    print("Nama:", person["first_name"], person["last_name"])
    print("Umur:", person["age"])
    print("Kota:", person["city"])
    print("Pekerjaan:", person["occupation"])
    print("Hobi:", person["hobby"])
    print()