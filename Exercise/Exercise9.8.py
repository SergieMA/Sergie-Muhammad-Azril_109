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
        print(f"Halo, {self.first_name}!")


class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Privileges admin:")

        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, city, job):
        super().__init__(first_name, last_name, age, city, job)
        self.privileges = Privileges()


admin = Admin("Sergie", "Azril", 18, "Karawang", "Mahasiswa")

admin.privileges.show_privileges()