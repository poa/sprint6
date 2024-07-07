from faker import Faker


class DataGenerator:
    def __init__(self):
        self.address = ""
        self.email = ""
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.phone = ""

        self.new_address()
        self.new_name()
        self.new_email()
        self.new_password()
        self.new_phone()

    def new_address(self):
        fake = Faker(["ru_RU"])
        self.address = fake.address()
        
    def new_name(self):
        fake = Faker(["ru_RU"])
        self.name = fake.name()
        self.first_name, self.last_name = self.name.split()
        return self.name

    def new_email(self):
        fake = Faker(["ru_RU"])
        self.email = fake.email()
        return self.email

    def new_password(self):
        fake = Faker()
        self.password = fake.password(length=8, special_chars=False)
        return self.password
    
    def new_phone(self):
        fake = Faker()
        self.phone = fake.phone_number()
        return self.phone

