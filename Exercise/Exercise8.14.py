def make_car(pabrikan, model, **informasi_tambahan):
    mobil = {}

    mobil['pabrikan'] = pabrikan
    mobil['model'] = model

    for kunci, nilai in informasi_tambahan.items():
        mobil[kunci] = nilai

    return mobil


mobil = make_car(
    'subaru',
    'outback',
    color='biru',
    tow_package=True
)

print(mobil)