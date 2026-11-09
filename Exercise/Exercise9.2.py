class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")


restaurant1 = Restaurant("Mie Gacoan", "Mie")
restaurant2 = Restaurant("Marugame Udon", "Udon")
restaurant3 = Restaurant("KFC", "Ayam")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()