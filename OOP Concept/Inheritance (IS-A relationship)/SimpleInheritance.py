class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()   # inherited method
dog.bark()  # child method


animal = Animal()
animal.eat()  # parent method