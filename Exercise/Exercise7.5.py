while True:
    umur = input("\nBerapa umur kamu? ")
    umur = int(umur)

    if umur < 3:
        print("Tiket gratis.")
    elif umur <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")