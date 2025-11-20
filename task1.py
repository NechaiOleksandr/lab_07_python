import datetime

class Person:
    def __init__(self, surname, firstName, birthDate, nickname = None):
        self.surname = surname
        self.first_name = firstName
        self.nickname = nickname

        parts = birthDate.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        self.birth_date = datetime.date(year, month, day)

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age = age - 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"


user1 = Person("Петро", "Петренко", "1990-05-20")
print(user1.get_fullname())
print(user1.get_age())

user2 = Person("Іван", "Іваненко", "2005-12-01", nickname="user123")
print(user2.get_fullname())
print(user2.get_age())