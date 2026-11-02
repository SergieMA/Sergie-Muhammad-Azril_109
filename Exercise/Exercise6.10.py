favorite_numbers = {
    "anisa": [20, 5, 12],
    "sergie": [18, 12, 14],
    "alma": [6, 2],
    "fadli": [3, 9, 18],
    "suruy": [2, 6, 20]
}

for name, numbers in favorite_numbers.items():
    print("Angka favorit", name.title() + ":")
    for number in numbers:
        print("-", number)
    print()