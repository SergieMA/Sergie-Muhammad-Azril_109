   
import json

with open("favorite_number.json") as file:
    favorite_number = json.load(file)

print(f"I know your favorite number! It's {favorite_number}.")