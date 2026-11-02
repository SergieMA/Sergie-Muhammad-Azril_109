Undangan_makan = ["Sulaiman", "Ekhsan", "Rara", "Samuel", "Kemala", "Aira"]
print("Sepertinya dinner kali ini aku hanya dapat mengundang 2 orang saja, maaf ya!")

Undangan_gagal = Undangan_makan.pop()
print(f"Maaf {Undangan_gagal}, aku tidak bisa mengundangmu untuk makan malam kali ini.")
Undangan_gagal = Undangan_makan.pop()
print(f"Maaf {Undangan_gagal}, aku tidak bisa mengundangmu untuk makan malam kali ini.")
Undangan_gagal = Undangan_makan.pop()
print(f"Maaf {Undangan_gagal}, aku tidak bisa mengundangmu untuk makan malam kali ini.")
Undangan_gagal = Undangan_makan.pop()
print(f"Maaf {Undangan_gagal}, aku tidak bisa mengundangmu untuk makan malam kali ini.")

print(f"Halo, {Undangan_makan[0]}! Kamu masih diundang untuk makan malam.")
print(f"Halo, {Undangan_makan[1]}! Kamu masih diundang untuk makan malam.")

del Undangan_makan[1]
del Undangan_makan[0]

print(Undangan_makan)