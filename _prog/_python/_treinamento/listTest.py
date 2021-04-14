import datetime
class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


my_list = [Person("Brayen Strong", datetime.date(1999, 7, 9), 170),
           Person("John Cena", datetime.date(1992, 7, 15), 180),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 178)]

print(my_list)


my_list2 = [{"name": "Brayen", "birthday": datetime.date(1999, 7, 9), "height": 170},
            {"name": "John Cena", "birthday": datetime.date(1992, 7, 15), "height": 180},
            {"name": "Chuck Norris", "birthday": datetime.date(1990, 8, 28), "height": 178}]

for i in my_list2:
    print(i.values())

