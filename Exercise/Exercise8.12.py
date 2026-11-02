def buat_sandwich(*bahan):
    print("\nSandwich yang dipesan:")
    for isi in bahan:
        print(f"- {isi}")


buat_sandwich('keju', 'telur')

buat_sandwich('daging sapi', 'saus', 'tomat')

buat_sandwich('ayam', 'keju', 'mayones', 'selada')