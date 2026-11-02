motor = "Suzuki"
nomor_motor = 12
daftar_motor = ["Suzuki", "Honda", "Yamaha"]

# Test equality and inequality with strings
print("apakah motor ini == 'Suzuki'? I predict True.")
print(motor == "Suzuki")

print("\napakah motor ini != 'honda'? I predict True.")
print(motor != "honda")

print("\napakah motornya == 'honda'? I predict False.")
print(motor == "honda")

print("\napakah motornya != 'Suzuki'? I predict False.")
print(motor != "Suzuki")

# Test using lower()
print("\napakah motor.lower() == 'suzuki'? I predict True.")
print(motor.lower() == "suzuki")

print("\napakah motor.lower() == 'honda'? I predict False.")
print(motor.lower() == "honda")

# Numerical tests
print("\napakah nomornya == 12? I predict True.")
print(nomor_motor == 12)

print("\napakah nomornya != 5? I predict True.")
print(nomor_motor != 5)

print("\napakah nomornya > 5? I predict True.")
print(nomor_motor > 5)

print("\napakah nomornya < 15? I predict True.")
print(nomor_motor < 15)

print("\napakah nomornya >= 12? I predict True.")
print(nomor_motor >= 12)

print("\napakah nomornya <= 12? I predict True.")
print(nomor_motor <= 12)

print("\napakah nomornya < 5? I predict False.")
print(nomor_motor < 5)

print("\napakah nomornya == 5? I predict False.")
print(nomor_motor == 5)

print("\napakah nomornya >= 15? I predict False.")
print(nomor_motor >= 15)

print("\napakah nomornya <= 5? I predict False.")
print(nomor_motor <= 5)

print("\napakah nomornya > 15? I predict False.")
print(nomor_motor > 15)

print("\napakah nomornya != 12? I predict False.")
print(nomor_motor != 12)

# Test using and
print("\napakah motor == 'Suzuki' and nomor_motor == 12? I predict True.")
print(motor == "Suzuki" and nomor_motor == 12)

print("\napakah motor == 'Honda' and nomor_motor == 12? I predict False.")
print(motor == "Honda" and nomor_motor == 12)

# Test using or
print("\napakah motor == 'Honda' or nomor_motor == 12? I predict True.")
print(motor == "Honda" or nomor_motor == 12)

print("\napakah motor == 'Honda' or nomor_motor == 5? I predict False.")
print(motor == "Honda" or nomor_motor == 5)

# Test using in
print("\napakah 'Suzuki' ada di daftar_motor? I predict True.")
print("Suzuki" in daftar_motor)

print("\napakah 'Kawasaki' ada di daftar_motor? I predict False.")
print("Kawasaki" in daftar_motor)

# Test using not in
print("\napakah 'Kawasaki' tidak ada di daftar_motor? I predict True.")
print("Kawasaki" not in daftar_motor)

print("\napakah 'Honda' tidak ada di daftar_motor? I predict False.")
print("Honda" not in daftar_motor)