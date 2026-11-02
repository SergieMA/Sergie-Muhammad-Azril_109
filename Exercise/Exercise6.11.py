cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": "sekitar 10,7 juta jiwa",
        "fact": "Merupakan pusat kegiatan ekonomi Indonesia."
    },

    "Bandung": {
        "country": "Indonesia",
        "population": "sekitar 2,5 juta jiwa",
        "fact": "Dikenal sebagai Kota Kembang."
    },

    "Surakarta": {
        "country": "Indonesia",
        "population": "sekitar 0,53 juta jiwa",
        "fact": "Dikenal sebagai salah satu pusat kebudayaan Jawa."
    }
}

for city, information in cities.items():
    print("Nama kota:", city)
    print("Negara:", information["country"])
    print("Jumlah penduduk:", information["population"])
    print("Fakta:", information["fact"])
    print()