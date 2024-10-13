
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name} кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        return self.__add__(value)
    def __radd__(self, value):
        return self.__add__(value)

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Бобры,', 15)
h2 = House('Домик в горах,',5)

print(h1)
print(h2)
#__eq__
print(h1 == h2)
#__add__
h1 = h1 + 3
print(h1)
h2.number_of_floors = 18
print(h1 == h2)
#__iadd__
h2 += 1
print(h2)
#__radd__
h1 = 4 + h1
print(h1)
#__lt__
print(h2 < h1)
#__le__
h1.number_of_floors = 5
print(h1 <= h2)
#__gt__
h2.number_of_floors = 13
print(h1 > h2)
#__ge__
print(h1 >= h2)
#__ne__
print(h1 != h2)




















