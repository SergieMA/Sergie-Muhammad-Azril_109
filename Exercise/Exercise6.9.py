favorite_places = {
    "sergie": ["Pangalengan", "Bali", "Yogyakarta"],
    "varrel": ["Jakarta", "Jepang"],
    "raul": ["Salatiga", "Malang", "Semarang"]
}

for name, places in favorite_places.items():
    print("Tempat favorit", name.title() + ":")
    for place in places:
        print("-", place)
    print()