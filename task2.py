import datetime
import csv


class Person:
    def __init__(self, surname, firstName, birthDate, nickname=None):
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


def modifier(filename):
    persons_objects = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            surname = row[0]
            firstName = row[1]
            birthDate = row[2]

            nickname = None
            if len(row) > 3:
                nickname = row[3]

            person = Person(surname, firstName, birthDate, nickname)
            persons_objects.append(person)

    with open(filename, 'w', encoding='utf-8', newline='') as f:

        for p in persons_objects:
            row_data = []
            row_data.append(p.surname)
            row_data.append(p.first_name)
            row_data.append(p.get_fullname())
            row_data.append(str(p.birth_date))

            if p.nickname:
                row_data.append(p.nickname)
            else:
                row_data.append("")
            row_data.append(p.get_age())

            f.write(",".join(row_data) + "\n")

with open("file.txt", 'w', encoding='utf-8') as f:
    data_row_1 = ["Петренко", "Петро", "1990-05-20", ""]
    f.write(",".join(data_row_1) + "\n")
    data_row_2 = ["Іваненко", "Іван", "2005-12-01", "user123"]
    f.write(",".join(data_row_2) + "\n")

modifier("file.txt")