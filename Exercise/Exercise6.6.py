favorite_languages = {
    "anisa": "python",
    "sergie": "java",
    "azril": "c",
    "sule": "python",
    "neon": "javascript"
}

people = ["jaden", "sergie", "sule", "anisa", "neon", "budi"]

for person in people:
    if person in favorite_languages:
        print(f"Terimakasih, {person.title()}, sudah mengikuti polling.")
    else:
        print(f"{person.title()}, silahkan mengikuti polling bahasa favorit Anda.")