from datetime import datetime, timedelta
from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker(["ru_RU"])
        self.address = ""
        self.email = ""
        self.name = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.phone = ""
        self.comment = ""
        self.date = ""

        self.new_address()
        self.new_name()
        self.new_email()
        self.new_password()
        self.new_phone()
        self.new_comment()
        self.new_date()

    def new_address(self):
        self.address = self.fake.street_address().replace("/", "")
        return self.address

    def new_name(self):
        self.name = self.fake.name().replace("-", "")
        self.first_name = self.name.split()[:1]
        self.last_name = self.name.split()[-1:]
        return self.name

    def new_email(self):
        self.email = self.fake.email()
        return self.email

    def new_password(self):
        self.password = self.fake.password(length=8, special_chars=False)
        return self.password

    def new_phone(self):
        self.phone = "+7" + str(self.fake.random_number(10, True))
        return self.phone

    def new_comment(self):
        self.comment = self.fake.sentence()
        return self.comment

    def new_date(self):
        start_date = datetime.today()
        end_date = start_date + timedelta(days=7)
        self.date = self.fake.date_between(start_date, end_date).__str__()
        return self.date
