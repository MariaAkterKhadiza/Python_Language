class Vehicle:
    def __init__(self, color, year):
        self.color = color
        self.year = year

class Car(Vehicle):
    def __init__(self, color, year, model):
        super().__init__(color, year)
        self.model = model



vehicle = Vehicle("red", 2023)
car = Car("Blue", 2023, "Toyota")


print(vehicle.color, vehicle.year)
print(car.color, car.year, car.model)
