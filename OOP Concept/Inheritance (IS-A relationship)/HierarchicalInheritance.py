class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

class Bird(Animal):
    def chirp(self):
        print("Bird is chirping")

dog = Dog()
dog.speak()  # inherited method from Animal
dog.bark()   # child method from Dog

cat = Cat()
cat.speak()  # inherited method from Animal
cat.meow()   # child method from Cat

bird = Bird()
bird.speak()  # inherited method from Animal
bird.chirp()  # child method from Bird

