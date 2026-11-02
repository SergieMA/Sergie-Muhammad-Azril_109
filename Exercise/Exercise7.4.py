prompt = "\nMasukkan topping pizza yang kamu inginkan dibawah ini"
prompt += "\nKetik 'quit' jika tidak ingin menambahkan topping: "

topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"Saya akan menambahkan {topping} ke pizza kamu.")