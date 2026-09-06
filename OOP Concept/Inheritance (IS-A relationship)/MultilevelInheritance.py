class Animal:
    def move(self):
        print("Animal is moving")
class Mammal(Animal):
    def feed_milk(self):
        print("Mammal is feeding milk")
class Dog(Mammal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.move()      # inherited method from Animal
dog.feed_milk() # inherited method from Mammal
dog.bark()      # child method from Dog

mammal = Mammal()
mammal.move()      # inherited method from Animal
mammal.feed_milk() # inherited method from Mammal
