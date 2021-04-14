from enum import Enum

class Car(Enum):
    ferari = 2
    bulgate = 3
    bmw = 5

print('Ferrari: {}'.format(Car.ferari.value))
print('Bulgate: {}'.format(Car.bulgate.value))
print('BMW: {}'.format(Car.bmw.value))

