class User:
    def __init__(self, first_name, last_name, age, city, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.job = job

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Pekerjaan: {self.job}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")


user1 = User("Sergie", "Azril", 18, "Karawang", "Mahasiswa")
user2 = User("Raka", "Pratama", 19, "Bandung", "Mahasiswa")
user3 = User("Dimas", "Saputra", 20, "Jakarta", "Mahasiswa")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()