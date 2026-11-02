rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe following rivers are included:")
for river in rivers.keys():
    print(river.title())

print("\nThe following countries are included:")
for country in rivers.values():
    print(country.title())