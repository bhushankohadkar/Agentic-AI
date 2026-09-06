class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def honk(self):
        print("Car is honking")

car = Car()
car.start()  # inherited method from Vehicle
car.honk()   # child method from Car