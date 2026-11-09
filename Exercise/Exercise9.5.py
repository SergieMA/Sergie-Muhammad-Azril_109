class User:
    def __init__(self, first_name, last_name, age, city, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Pekerjaan: {self.job}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Sergie", "Azril", 18, "Karawang", "Mahasiswa")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts: {user.login_attempts}")