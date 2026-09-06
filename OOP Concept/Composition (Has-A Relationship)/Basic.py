class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start(self):
        self.engine.start()  # Delegating the start method to the Engine class

my_car = Car()
my_car.start()  # Output: Engine started.