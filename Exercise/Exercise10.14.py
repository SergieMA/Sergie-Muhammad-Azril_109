import json

def get_new_username():
    username = input("Masukkan username baru: ")

    with open("username.json", "w") as file:
        json.dump(username, file)

    return username


def greet_user():
    try:
        with open("username.json") as file:
            username = json.load(file)

    except FileNotFoundError:
        username = get_new_username()

    else:
        print(f"Apakah username kamu {username}?")
        answer = input("Masukkan yes atau no: ")

        if answer == "no":
            username = get_new_username()

    print(f"Selamat datang kembali, {username}!")


greet_user()