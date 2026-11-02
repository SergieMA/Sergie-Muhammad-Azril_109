jawaban_survei = {}

survei_aktif = True

while survei_aktif:
    nama = input("\nSiapa nama kamu? ")

    tempat_impian = input("Jika kamu bisa mengunjungi satu tempat di dunia, ke mana kamu ingin pergi? ")

    jawaban_survei[nama] = tempat_impian

    lanjut_survei = input("Apakah kamu ingin mengizinkan orang lain mengisi survei? (ya/tidak) ")

    if lanjut_survei == 'tidak':
        survei_aktif = False

print("\n--- Hasil Survei ---")

for nama, tempat in jawaban_survei.items():
    print(f"{nama} ingin mengunjungi {tempat}.")
    
