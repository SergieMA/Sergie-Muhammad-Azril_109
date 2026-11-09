class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["coklat", "vanila", "stroberi", "matcha"]

    def show_flavors(self):
        print("Rasa es krim yang tersedia:")

        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("Ice Cream Corner", "Dessert")
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()

ice_cream_stand.show_flavors()