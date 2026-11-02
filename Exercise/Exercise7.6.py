# Cara Pertama
topping = ""

while topping != "quit":
    topping = input("\nMasukkan topping pizza: ")

    if topping != "quit":
        print(f"Saya akan menambahkan {topping} ke pizza kamu.")
        
# Cara Kedua
active = True
while active:
    topping = input("\nMasukkan topping pizza: ")

    if topping == "quit":
        active = False
    else:
        print(f"Saya akan menambahkan {topping} ke pizza kamu.")
        
# Cara Ketiga
while True:
    topping = input("\nMasukkan topping pizza: ")

    if topping == "quit":
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza kamu.")