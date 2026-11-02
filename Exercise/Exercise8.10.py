pesan = [
    'Selamat pagi!',
    'Jangan lupa belajar.',
    'Tetap semangat!',
    'Terus berusaha!'
]

sent_messages = []

def send_messages(pesan, sent_messages):
    while pesan:
        pesan_saat_ini = pesan.pop()

        print(pesan_saat_ini)

        sent_messages.append(pesan_saat_ini)


send_messages(pesan, sent_messages)

print("\nDaftar pesan awal:")
print(pesan)

print("\nDaftar pesan terkirim:")
print(sent_messages)