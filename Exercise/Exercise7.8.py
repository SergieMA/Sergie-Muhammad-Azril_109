sandwich_orders = ['tuna', 'daging sapi', 'ayam', 'telur']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Saya sudah membuat sandwich {current_sandwich}.")

    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich)