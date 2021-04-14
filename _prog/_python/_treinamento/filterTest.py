collection = [('Car', 10), ('MotorBike', 2), ('Ship', 1)]
a = (c for c in collection if not c[1] < 20)
print(next(a))
