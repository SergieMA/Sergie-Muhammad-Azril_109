pesanan_sandwich = [
    'tuna', 'pastrami', 'daging sapi',
    'pastrami', 'ayam', 'pastrami', 'telur'
]

sandwich_selesai = []

print("Maaf, kedai sudah kehabisan pastrami.")

while 'pastrami' in pesanan_sandwich:
    pesanan_sandwich.remove('pastrami')

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()

    print(f"Saya sudah membuat sandwich {sandwich_saat_ini}.")

    sandwich_selesai.append(sandwich_saat_ini)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)