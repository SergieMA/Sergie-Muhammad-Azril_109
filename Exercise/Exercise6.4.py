glossary = {
    "variable": "Nama yang digunakan untuk menyimpan sebuah nilai.",
    "list": "Kumpulan beberapa item yang disimpan dalam satu variabel.",
    "loop": "Perintah untuk mengulang suatu bagian kode.",
    "if statement": "Perintah untuk memeriksa suatu kondisi.",
    "dictionary": "Kumpulan data yang disimpan dalam pasangan key dan value.",
    "string": "Tipe data yang digunakan untuk menyimpan teks.",
    "integer": "Tipe data yang digunakan untuk menyimpan bilangan bulat.",
    "float": "Tipe data yang digunakan untuk menyimpan bilangan desimal.",
    "boolean": "Tipe data yang memiliki nilai True atau False.",
    "function": "Sekumpulan kode yang dibuat untuk menjalankan tugas tertentu."
}

for word, meaning in glossary.items():
    print(word.title() + ":")
    print(meaning + "\n")