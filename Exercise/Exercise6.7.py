person_1 = {
    "first_name": "Sergie Muhammad",
    "last_name": "Azril",
    "age": 18,
    "city": "Karawang"
}

person_2 = {
    "first_name": "Rahmat",
    "last_name": "Hidayat",
    "age": 19,
    "city": "Karawang"
}

person_3 = {
    "first_name": "Yanti",
    "last_name": "Aulia",
    "age": 20,
    "city": "Bandung"
}

people = [person_1, person_2, person_3]

for person in people:
    print("Nama depan:", person["first_name"])
    print("Nama belakang:", person["last_name"])
    print("Umur:", person["age"])
    print("Kota:", person["city"])
    print()