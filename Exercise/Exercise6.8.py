pet_1 = {
    "animal": "Kucing",
    "owner": "Tisa"
}

pet_2 = {
    "animal": "Gekko",
    "owner": "Sergie"
}

pet_3 = {
    "animal": "Kelinci",
    "owner": "Mail"
}

pet_4 = {
    "animal": "Burung",
    "owner": "Yunus"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print("Jenis hewan:", pet["animal"])
    print("Pemilik:", pet["owner"])
    print()