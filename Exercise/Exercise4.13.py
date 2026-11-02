buffet_minuman = ("thai tea", "ocha", "lemon tea", "es teh", "permen karet")

print("Menu minuman :")
for x in buffet_minuman:
    print(x)

# Percobaan mengubah item. Baris ini sengaja dijadikan komentar
# agar program tetap jalan. Hapus tanda # untuk melihat error.
# buffet_foods[0] = "green tea"
# TypeError: 'tuple' object does not support item assignment

buffet_minuman = ("thai tea", "milo", "lemon tea", "air putih", "permen karet")

print("\nMenu minuman yang baru:")
for x in buffet_minuman:
    print(x)