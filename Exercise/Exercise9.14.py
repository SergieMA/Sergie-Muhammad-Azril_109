from random import choice

lottery_items = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

winning_ticket = []

for i in range(4):
    item = choice(lottery_items)
    winning_ticket.append(item)

print(f"Nomor dan huruf pemenang: {winning_ticket}")

print("Tiket yang cocok dengan 4 elemen ini memenangkan hadiah!")