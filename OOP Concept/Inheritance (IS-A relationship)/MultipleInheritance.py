class Flyer:
    def fly(self):
        print("Flying in the sky!")
class Swimmer:
    def swim(self):
        print("Swimming in the water!")
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck is quacking!")

duck = Duck()
duck.fly()   # inherited method from Flyer
duck.swim()  # inherited method from Swimmer
duck.quack() # child method from Duck