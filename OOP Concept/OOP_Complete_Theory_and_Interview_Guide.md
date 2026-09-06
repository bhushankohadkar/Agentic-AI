# Complete OOP: Concepts, Theory, and Interview Questions

## TABLE OF CONTENTS
1. [Fundamentals](#fundamentals)
2. [Classes and Objects](#classes-and-objects)
3. [Encapsulation](#encapsulation)
4. [Inheritance](#inheritance)
5. [Polymorphism](#polymorphism)
6. [Abstraction](#abstraction)
7. [Advanced Concepts](#advanced-concepts)
8. [Interview Questions & Answers](#interview-questions--answers)
9. [System Design Examples](#system-design-examples)

---

# FUNDAMENTALS

## What is OOP?

**Object-Oriented Programming** is a programming paradigm that organizes code around **objects** and **classes** rather than functions and logic.

### Core Philosophy
> Code should model real-world entities, with properties (data) and behaviors (methods) encapsulated together.

### Why OOP?

| Problem | Solution |
|---------|----------|
| Code repetition | **Inheritance** - reuse common code |
| Unorganized data | **Encapsulation** - group related data & methods |
| Rigid behavior | **Polymorphism** - different implementations of same interface |
| Complex systems | **Abstraction** - hide complexity, show essentials |

### Four Pillars of OOP

```
┌─────────────────────────────────────┐
│  ENCAPSULATION (Data Hiding)        │
│  - Group data + methods             │
│  - Control access (public/private)  │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  ABSTRACTION (Complexity Hiding)    │
│  - Hide implementation details      │
│  - Show only essential features     │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  INHERITANCE (Code Reuse)           │
│  - Parent-child relationships       │
│  - Extend existing classes          │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  POLYMORPHISM (Flexibility)         │
│  - Same interface, different forms  │
│  - Runtime behavior selection       │
└─────────────────────────────────────┘
```

---

# CLASSES AND OBJECTS

## Concept: Classes vs Objects

### Class
A **blueprint** or **template** for creating objects. Defines structure and behavior.

```python
class Dog:  # Class = Template
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"
```

### Object (Instance)
A **specific instance** of a class with actual data.

```python
buddy = Dog("Buddy")    # Object 1
max = Dog("Max")        # Object 2
```

**Analogy**: Class is a cookie cutter, object is the cookie.

---

## Object Lifecycle

```
1. CREATION
   ↓ __new__() creates memory space
   ↓ __init__() initializes object
   
2. USAGE
   ↓ Object exists in memory
   ↓ Methods can be called
   ↓ Attributes can be modified
   
3. DESTRUCTION
   ↓ Reference count → 0
   ↓ __del__() cleanup
   ↓ Garbage collection
```

### Example

```python
class Person:
    def __init__(self, name):
        print(f"Creating {name}")
        self.name = name
    
    def __del__(self):
        print(f"Deleting {self.name}")

# Creation
p = Person("Alice")  # Output: Creating Alice

# Usage
print(p.name)  # Alice

# Destruction
del p  # Output: Deleting Alice
```

---

## Methods in a Class

### Instance Methods
Operate on **specific instance** data. Receive `self`.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):  # Instance method
        self.balance += amount
        return f"New balance: {self.balance}"

account = Account(1000)
print(account.deposit(500))  # Works with specific account
```

### Class Methods
Operate on **class-level** data. Receive `cls`.

```python
class Account:
    interest_rate = 0.05  # Class variable
    
    @classmethod
    def from_string(cls, string_data):
        # Create instance from string
        return cls(float(string_data))

acc = Account.from_string("1000.00")
```

### Static Methods
No access to `self` or `cls`. Just utility functions.

```python
class Utils:
    @staticmethod
    def add(a, b):  # No self or cls
        return a + b

print(Utils.add(2, 3))  # 5
```

### Property Decorators
Access methods like attributes.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature(0)
print(temp.fahrenheit)  # 32 (read)
temp.fahrenheit = 32    # (write)
print(temp._celsius)    # 0
```

---

# ENCAPSULATION

## Concept: Data Hiding

**Encapsulation** = Bundle data + methods together + Control access

### Three Levels of Access

```python
class BankAccount:
    def __init__(self, balance):
        self.public_info = "Account"      # Public (anyone can access)
        self._protected_info = balance    # Protected (use with caution)
        self.__private_balance = balance  # Private (class only)
    
    def get_balance(self):
        return self.__private_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__private_balance += amount
            return True
        return False
```

### Access Control

| Access Level | Symbol | Access From | Use Case |
|------------|--------|------------|----------|
| **Public** | `name` | Anywhere | Public API, use freely |
| **Protected** | `_name` | Class + Subclass | Internal use, caution needed |
| **Private** | `__name` | Class only | Sensitive data, no direct access |

### Name Mangling
Python doesn't truly enforce privacy but uses **name mangling**:

```python
class Account:
    def __init__(self):
        self.__balance = 1000

acc = Account()
print(acc.__balance)           # ❌ AttributeError
print(acc._Account__balance)   # ✅ Works (name mangling)
```

---

## Benefits of Encapsulation

### 1. Data Validation
```python
class Age:
    def __init__(self, years):
        self.__age = 0
        self.set_age(years)
    
    def set_age(self, years):
        if 0 < years < 150:
            self.__age = years
        else:
            raise ValueError("Invalid age")
    
    def get_age(self):
        return self.__age

person = Age(25)
person.set_age(300)  # ❌ ValueError
```

### 2. Consistency
```python
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def area(self):
        """Always calculated from width and height"""
        return self.__width * self.__height

rect = Rectangle(5, 10)
print(rect.area())  # 50 (always correct)
```

### 3. Flexibility
```python
class User:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name.upper()  # Can transform before returning
    
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value

user = User("alice")
print(user.name)  # ALICE
```

---

# INHERITANCE

## Concept: Code Reuse Through Hierarchy

**Inheritance** = Child class inherits parent class features and can override them.

### Why Inheritance?

```
Problem: Code Duplication
├── Car has: color, speed, accelerate()
├── Truck has: color, speed, accelerate()  ← Same!
└── Motorcycle has: color, speed, accelerate()

Solution: Vehicle (Parent)
├── Car (Child)
├── Truck (Child)
└── Motorcycle (Child)
```

### Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):  # Inherits from Animal
    def speak(self):  # Override
        return f"{self.name} barks: Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy barks: Woof!
```

---

## Types of Inheritance

### 1. Single Inheritance
One child, one parent.

```python
class Vehicle:
    pass

class Car(Vehicle):
    pass
```

### 2. Multi-Level Inheritance
Grandparent → Parent → Child

```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass
```

### 3. Multiple Inheritance
Multiple parents.

```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmer):
    pass

duck = Duck()
print(duck.fly())    # Flying
print(duck.swim())   # Swimming
```

### 4. Hierarchical Inheritance
One parent, multiple children.

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass
```

### 5. Hybrid Inheritance
Combination of types.

```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Flyable:
    pass

class Bat(Mammal, Flyable):
    pass
```

---

## super() and Method Resolution Order (MRO)

### super() Function
Call parent class methods.

```python
class Parent:
    def method(self):
        return "Parent"

class Child(Parent):
    def method(self):
        parent_result = super().method()
        return parent_result + " + Child"

child = Child()
print(child.method())  # Parent + Child
```

### Method Resolution Order (MRO)
Order Python searches for methods in multiple inheritance.

```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
# [D, B, C, A, object]
#  ↑  ↑  ↑  ↑  ↑
#  |  |  |  |  └─ All objects inherit from object
#  |  |  |  └──── Parent of both B and C
#  |  |  └─────── Right parent
#  |  └────────── Left parent
#  └───────────── Current class
```

---

# POLYMORPHISM

## Concept: Many Forms, One Interface

**Polymorphism** = "Poly" (many) + "Morph" (form)

Same method name, different behavior based on object type.

### Example

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Polymorphic call
shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())  # Different behavior, same method
```

---

## Types of Polymorphism

### 1. Compile-Time Polymorphism (Method Overloading)
Python doesn't support true overloading, but we simulate it:

```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))        # 3
print(calc.add(1, 2, 3, 4))  # 10
```

### 2. Runtime Polymorphism (Method Overriding)
Subclass overrides parent method.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphic function
def make_speak(animal):
    print(animal.speak())  # Works with ANY object that has speak()

make_speak(Dog())  # Woof!
make_speak(Cat())  # Meow!
```

### 3. Duck Typing
"If it walks like a duck and quacks like a duck, it's a duck."

```python
class Dog:
    def speak(self):
        return "Woof"

class Person:
    def speak(self):
        return "Hello"

def make_sound(entity):
    return entity.speak()

print(make_sound(Dog()))    # Woof (not inherited, but has speak())
print(make_sound(Person())) # Hello (different class, same interface)
```

### 4. Operator Overloading
Redefine operators for custom classes.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # (4, 6) - uses __add__
```

---

# ABSTRACTION

## Concept: Hiding Complexity

**Abstraction** = Show only essential features, hide implementation details.

### Real-World Example

```
User sees:        │ Implementation
──────────────────┼─────────────────────
Press power       │ Sends signal to CPU
button            │ CPU powers on GPU
                  │ GPU initializes
                  │ Memory checks
                  │ Boot sequence
                  │ ... (100+ steps)
```

### Python: Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

# animal = Animal()  # ❌ TypeError: Can't instantiate abstract class
dog = Dog()         # ✅ Works
```

### Benefits of Abstraction

1. **Simplicity** - Users don't need to know implementation
2. **Maintainability** - Can change implementation without breaking interface
3. **Security** - Hide sensitive implementation details
4. **Consistency** - Force subclasses to implement required methods

---

## Example: Database Abstraction

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass
    
    @abstractmethod
    def close(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Connecting to MySQL...")
    
    def query(self, sql):
        print(f"Executing MySQL: {sql}")
    
    def close(self):
        print("Closing MySQL connection")

class MongoDB(Database):
    def connect(self):
        print("Connecting to MongoDB...")
    
    def query(self, sql):
        print(f"Executing MongoDB: {sql}")
    
    def close(self):
        print("Closing MongoDB connection")

# Use either database with same interface
def fetch_data(db: Database):
    db.connect()
    db.query("SELECT * FROM users")
    db.close()

fetch_data(MySQL())     # Works
fetch_data(MongoDB())   # Works
```

---

# ADVANCED CONCEPTS

## Composition vs Inheritance

### Inheritance (IS-A)
```python
class Animal:
    pass

class Dog(Animal):  # Dog IS-A Animal
    pass
```

### Composition (HAS-A)
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine started
```

### When to Use Each

| Inheritance | Composition |
|------------|-------------|
| Clear IS-A relationship | Flexible HAS-A relationship |
| Share common behavior | Behavior changes at runtime |
| 2-3 levels max | No depth limit |
| Tight coupling | Loose coupling |
| "Is a type of" | "Uses a" |

### Example Decision

```python
# ❌ Bad: Inheritance for wrong reason
class Car(Engine):  # Car should NOT inherit from Engine
    pass

# ✅ Good: Composition
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

# ✅ Good: Inheritance for right reason
class Vehicle:
    pass

class Car(Vehicle):  # Car IS-A Vehicle
    pass
```

---

## Multiple Inheritance and Diamond Problem

### Diamond Problem

```
        A
       / \
      B   C
       \ /
        D

Question: Which method from A does D use?
```

### Python Solves with MRO

```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # [D, B, C, A, object]
d = D()
print(d.method())  # A (follows MRO)
```

### Cooperative Multiple Inheritance

```python
class Mixin1:
    def __init__(self):
        super().__init__()
        self.mixin1 = True

class Mixin2:
    def __init__(self):
        super().__init__()
        self.mixin2 = True

class Base:
    def __init__(self):
        self.base = True

class Combined(Mixin1, Mixin2, Base):
    def __init__(self):
        super().__init__()

obj = Combined()
print(obj.mixin1, obj.mixin2, obj.base)  # True, True, True
```

---

## Dunder Methods (Magic Methods)

Special methods that Python calls automatically.

### Object Initialization & Representation

```python
class Person:
    def __init__(self, name, age):      # Constructor
        self.name = name
        self.age = age
    
    def __str__(self):                   # For print()
        return f"{self.name}, {self.age}"
    
    def __repr__(self):                  # For debugging
        return f"Person('{self.name}', {self.age})"
    
    def __del__(self):                   # Destructor
        print(f"Deleting {self.name}")

p = Person("Alice", 25)
print(p)          # Alice, 25 (uses __str__)
print(repr(p))    # Person('Alice', 25) (uses __repr__)
del p             # Deleting Alice (uses __del__)
```

### Comparison Operators

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def __eq__(self, other):  # ==
        return self.gpa == other.gpa
    
    def __lt__(self, other):  # <
        return self.gpa < other.gpa
    
    def __le__(self, other):  # <=
        return self.gpa <= other.gpa

s1 = Student("Alice", 3.8)
s2 = Student("Bob", 3.8)
s3 = Student("Carol", 3.5)

print(s1 == s2)  # True (same GPA)
print(s1 < s3)   # False (s1 has higher GPA)
```

### Arithmetic Operators

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Money(self.amount + other.amount)
    
    def __sub__(self, other):
        return Money(self.amount - other.amount)
    
    def __mul__(self, num):
        return Money(self.amount * num)
    
    def __str__(self):
        return f"${self.amount:.2f}"

m1 = Money(100)
m2 = Money(50)

print(m1 + m2)  # $150.00
print(m1 - m2)  # $50.00
print(m1 * 2)   # $200.00
```

### Container Methods

```python
class Inventory:
    def __init__(self):
        self.items = []
    
    def __len__(self):              # len()
        return len(self.items)
    
    def __getitem__(self, index):   # []
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __contains__(self, item):   # in
        return item in self.items
    
    def __iter__(self):             # for loop
        return iter(self.items)

inv = Inventory()
inv.items = ["apple", "banana", "orange"]

print(len(inv))          # 3
print(inv[0])            # apple
print("banana" in inv)   # True

for item in inv:
    print(item)
```

### Callable Objects

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

times_three = Multiplier(3)
print(times_three(5))  # 15
print(times_three(10)) # 30
```

---

## Property Decorators

Control attribute access with getter/setter.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return (self._celsius * 9/5) + 32
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def kelvin(self):
        """Read-only property"""
        return self._celsius + 273.15

temp = Temperature(0)
print(temp.celsius)     # 0 (getter)
print(temp.fahrenheit)  # 32.0 (computed property)
temp.celsius = 100      # setter
print(temp.fahrenheit)  # 212.0
print(temp.kelvin)      # 373.15 (read-only)
```

---

# INTERVIEW QUESTIONS & ANSWERS

## LEVEL 1: Fundamentals

### Q1: What is OOP? Why is it important?

**Answer:**
Object-Oriented Programming is a paradigm that organizes code around objects (entities with state and behavior) rather than functions and logic. 

**Why important:**
- **Modularity**: Code organized into reusable objects
- **Maintainability**: Easier to understand and modify
- **Scalability**: Systems grow without exponential complexity
- **Reusability**: Code written once, used many times
- **Real-world mapping**: Objects mirror real-world entities

**Example:**
```python
# Procedural (Bad)
users = []
def add_user(user_list, name, age):
    user_list.append({"name": name, "age": age})

# OOP (Good)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

users = [User("Alice", 25), User("Bob", 30)]
```

---

### Q2: Difference between class and object?

**Answer:**

| Aspect | Class | Object |
|--------|-------|--------|
| **What is it** | Blueprint/Template | Instance of a class |
| **Memory** | No memory allocated | Memory allocated |
| **Creation** | Defined once | Can create many |
| **Example** | Cookie cutter | Actual cookie |

**Code:**
```python
class Dog:  # Class - template
    def bark(self):
        return "Woof!"

buddy = Dog()  # Object - instance
max = Dog()    # Another object
```

---

### Q3: What are the four pillars of OOP?

**Answer:**

1. **Encapsulation** - Bundle data + methods, control access
2. **Abstraction** - Hide complexity, show only essentials
3. **Inheritance** - Reuse code through parent-child relationship
4. **Polymorphism** - Same interface, different behavior

**Quick Example:**
```python
# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

# Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Inheritance
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism
def make_sound(animal: Animal):
    print(animal.speak())  # Works with any Animal subclass
```

---

## LEVEL 2: Encapsulation

### Q4: What is encapsulation and its benefits?

**Answer:**
Encapsulation is bundling data (attributes) and methods together within a class and controlling access through access modifiers.

**Benefits:**
1. **Data Protection**: Prevent unauthorized access
2. **Validation**: Control how data is modified
3. **Flexibility**: Change implementation without affecting users
4. **Maintainability**: Easier to update code

**Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)           # ✅ Works
print(acc.get_balance())   # 1500
print(acc.__balance)       # ❌ AttributeError
```

---

### Q5: Difference between private, protected, and public?

**Answer:**

| Access Level | Symbol | Accessible From | Use Case |
|------------|--------|-----------------|----------|
| **Public** | `name` | Anywhere | Public interface, public API |
| **Protected** | `_name` | Class + Subclass | Internal use, inheritance chain |
| **Private** | `__name` | Class only | Sensitive data, complete control |

**Python Note:** Python doesn't enforce privacy (unlike Java/C++), but uses name mangling as convention.

**Example:**
```python
class Person:
    def __init__(self, name, age, ssn):
        self.name = name              # Public
        self._age = age               # Protected
        self.__ssn = ssn              # Private
    
    def get_ssn(self):
        return self.__ssn

person = Person("Alice", 25, "123-45-6789")
print(person.name)           # Alice (public, OK)
print(person._age)           # 25 (protected, works but not recommended)
print(person.__ssn)          # ❌ AttributeError (private, blocked)
print(person.get_ssn())      # 123-45-6789 (through method, OK)
```

---

### Q6: What are getters and setters? Why use them?

**Answer:**
Getters and setters are methods to access and modify private attributes safely.

**Why use:**
- Validate data before setting
- Compute values on the fly
- Track changes
- Maintain consistency

**Example:**
```python
class Age:
    def __init__(self, years):
        self.__years = 0
        self.set_age(years)
    
    def get_age(self):  # Getter
        return self.__years
    
    def set_age(self, years):  # Setter
        if 0 < years < 150:
            self.__years = years
        else:
            raise ValueError("Invalid age")

age = Age(25)
print(age.get_age())  # 25
age.set_age(200)      # ❌ ValueError: Invalid age

# Better with properties:
class Age:
    def __init__(self, years):
        self._years = 0
        self.years = years  # Use property
    
    @property
    def years(self):
        return self._years
    
    @years.setter
    def years(self, value):
        if 0 < value < 150:
            self._years = value
        else:
            raise ValueError("Invalid age")

age = Age(25)
print(age.years)  # 25 (looks like attribute, works like method)
age.years = 200   # ❌ ValueError
```

---

## LEVEL 3: Inheritance

### Q7: What is inheritance? What problem does it solve?

**Answer:**
Inheritance allows a class (child) to acquire properties and methods from another class (parent), enabling code reuse and establishing hierarchical relationships.

**Problems it solves:**
1. **Code Duplication** - Write once, inherit multiple times
2. **Maintainability** - Update common code in one place
3. **Hierarchy** - Model real-world relationships
4. **Extensibility** - Add new features through subclassing

**Example:**
```python
# Without inheritance (Bad)
class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Engine started")

class Truck:  # Duplicate code!
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Engine started")

# With inheritance (Good)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Engine started")

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass
```

---

### Q8: What are different types of inheritance?

**Answer:**
Five types with increasing complexity:

1. **Single** - One parent, one child
2. **Multi-level** - Grandparent → Parent → Child
3. **Multiple** - Multiple parents
4. **Hierarchical** - One parent, multiple children
5. **Hybrid** - Combination of types

**Examples:**

```python
# 1. Single
class Animal:
    pass

class Dog(Animal):
    pass

# 2. Multi-level
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# 3. Multiple
class Flyer:
    pass

class Swimmer:
    pass

class Duck(Flyer, Swimmer):
    pass

# 4. Hierarchical
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 5. Hybrid
class Base:
    pass

class Intermediate(Base):
    pass

class Flyer:
    pass

class Final(Intermediate, Flyer):
    pass
```

---

### Q9: What is super()? When do you use it?

**Answer:**
`super()` returns a proxy object that delegates method calls to a parent class. Used to call parent methods from child class.

**When to use:**
- Initialize parent class in child's `__init__`
- Extend parent method functionality
- Multiple inheritance with MRO

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent init
        self.breed = breed
    
    def speak(self):
        parent_sound = super().speak()  # Call parent method
        return f"{parent_sound} -> Woof!"

dog = Dog("Buddy", "Golden")
print(dog.speak())  # Some sound -> Woof!
```

**Why super() over hardcoding:**
```python
# ❌ Bad
class Dog(Animal):
    def speak(self):
        return Animal.speak(self) + " Woof!"

# ✅ Good (flexible with MRO)
class Dog(Animal):
    def speak(self):
        return super().speak() + " Woof!"
```

---

### Q10: What is Method Resolution Order (MRO)?

**Answer:**
MRO is the order Python searches for methods and attributes in a hierarchy, especially important in multiple inheritance.

**Rules (C3 Linearization):**
1. Child classes checked before parents
2. Order of inheritance preserved
3. Each class appears once

**Example:**
```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D.mro())
# [D, B, C, A, object]
#  ↑  ↑  ↑  ↑  ↑
#  |  |  |  |  └─ Every class inherits from object
#  |  |  |  └──── Common parent
#  |  |  └─────── Second parent
#  |  └────────── First parent
#  └───────────── Current class

print(D().method())  # "B" (D → B → C → A)
```

**View MRO:**
```python
print(D.mro())        # List form
print(D.__mro__)      # Tuple form
print(D.__class__.__mro__)  # Also works
```

---

## LEVEL 4: Polymorphism

### Q11: What is polymorphism? Explain with example.

**Answer:**
Polymorphism means "many forms" - same interface, different implementations based on object type.

**Benefits:**
- **Flexibility** - Same code works with different types
- **Maintainability** - Add new types without changing existing code
- **Extensibility** - Easy to extend functionality

**Example:**
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Polymorphic function
def print_area(shape: Shape):
    print(f"Area: {shape.area()}")

print_area(Circle(5))   # Circle's area() called
print_area(Square(4))   # Square's area() called
```

---

### Q12: What are different types of polymorphism?

**Answer:**

1. **Compile-Time Polymorphism** (Python doesn't truly support, but simulated)
2. **Runtime Polymorphism** (Method Overriding)
3. **Duck Typing** (Python specific)
4. **Operator Overloading** (Dunder methods)

**Examples:**

```python
# 1. Compile-Time (Simulated)
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))        # 3
print(calc.add(1, 2, 3, 4))  # 10

# 2. Runtime Polymorphism (Method Overriding)
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 3. Duck Typing
class Dog:
    def speak(self):
        return "Woof!"

class Person:
    def speak(self):
        return "Hello!"

def make_sound(entity):
    return entity.speak()  # Works with ANY object that has speak()

print(make_sound(Dog()))    # No inheritance needed!
print(make_sound(Person())) # Different class

# 4. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # (4, 6) - uses __add__
```

---

### Q13: Method Overriding vs Method Overloading

**Answer:**

| Feature | Overriding | Overloading |
|---------|-----------|------------|
| **Definition** | Child redefines parent method | Same method, different params |
| **Python Support** | Yes, native | No, must simulate |
| **Achieved By** | Inheritance | `*args`, `**kwargs` |
| **Invocation** | Based on type | Based on parameters |

**Overriding:**
```python
class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):  # Override
        return "Woof!"
```

**Overloading (Simulated):**
```python
class Calculator:
    def add(self, a, b, c=0):  # Optional parameter
        return a + b + c

calc = Calculator()
print(calc.add(1, 2))      # 3
print(calc.add(1, 2, 3))   # 6

# Better: using *args
class Calculator:
    def add(self, *args):  # Variable arguments
        return sum(args)

calc = Calculator()
print(calc.add(1))        # 1
print(calc.add(1, 2))     # 3
print(calc.add(1, 2, 3))  # 6
```

---

## LEVEL 5: Abstraction

### Q14: What is abstraction? How does it differ from encapsulation?

**Answer:**

| Aspect | Abstraction | Encapsulation |
|--------|------------|---------------|
| **Purpose** | Hide complexity | Hide data |
| **What it hides** | Implementation details | Internal state |
| **Focus** | Interface | Access control |
| **Example** | Don't show sorting algorithm | Hide password storage |

**Abstraction (What):**
```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Hide how payment is processed"""
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        # User doesn't need to know: encryption, validation, API calls, etc.
        return f"Processing ${amount} via credit card"
```

**Encapsulation (How):**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Hide internal balance
    
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print(acc.get_balance())   # 1000
print(acc.__balance)       # ❌ AttributeError
```

---

### Q15: Abstract Classes vs Interfaces

**Answer:**
Python doesn't have true interfaces, but Abstract Base Classes (ABC) serve the purpose.

| Feature | Abstract Class | Interface |
|---------|----------------|-----------|
| **Has implementation** | Yes, can have implemented methods | No, all abstract (Python uses ABC) |
| **Inheritance** | Single (usually) | Multiple |
| **Purpose** | Define common behavior | Define contract |
| **In Python** | `ABC` module | `ABC` module (no actual interface) |

**Example:**
```python
from abc import ABC, abstractmethod

# Abstract Class (can have some implementation)
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Implemented method
    
    @abstractmethod
    def speak(self):  # Abstract method
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Interface-like (all methods abstract)
class PaymentProcessor(ABC):
    @abstractmethod
    def validate(self):
        pass
    
    @abstractmethod
    def process(self, amount):
        pass
    
    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def validate(self):
        return True
    
    def process(self, amount):
        return f"Charged ${amount}"
    
    def refund(self, amount):
        return f"Refunded ${amount}"
```

---

## LEVEL 6: Advanced Concepts

### Q16: What is composition? When do you use it over inheritance?

**Answer:**
Composition means building complex objects from simpler objects (HAS-A relationship).

**Inheritance vs Composition:**

| Inheritance (IS-A) | Composition (HAS-A) |
|------------------|-------------------|
| Dog IS-A Animal | Car HAS-A Engine |
| Tight coupling | Loose coupling |
| Single path | Multiple paths |
| Fixed at compile time | Can change at runtime |

**Example:**

```python
# ❌ Bad: Wrong use of inheritance
class Engine:
    def start(self):
        return "Engine started"

class Car(Engine):  # Car should NOT inherit from Engine
    def drive(self):
        return "Driving"

# ✅ Good: Use composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        return self.engine.start()
    
    def drive(self):
        return "Driving"

car = Car()
print(car.start())  # Engine started
print(car.drive())  # Driving
```

**When to use composition:**
- Behavior changes at runtime
- No clear IS-A relationship
- Need flexibility
- Avoid deep hierarchies

---

### Q17: Diamond Problem in Multiple Inheritance

**Answer:**
Diamond Problem occurs when a class inherits from multiple parents that share a common ancestor.

**The Problem:**
```
        A
       / \
      B   C
       \ /
        D

Which A's method does D inherit?
```

**Python's Solution: MRO (C3 Linearization)**
```python
class A:
    def method(self):
        print("A.method()")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
# [D, B, C, A, object]

D().method()  # A.method() - follows MRO
```

**Best Practice: Use super()**
```python
class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        super().__init__()
        print("B.__init__")

class C(A):
    def __init__(self):
        super().__init__()
        print("C.__init__")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D.__init__")

D()
# Output:
# A.__init__
# C.__init__
# B.__init__
# D.__init__
# (follows MRO: D → B → C → A)
```

---

### Q18: What are dunder methods? Name some common ones.

**Answer:**
Dunder methods (double underscore) are special methods Python calls automatically for specific operations.

**Common Dunder Methods:**

```python
class Person:
    def __init__(self, name, age):      # Constructor
        self.name = name
        self.age = age
    
    def __str__(self):                   # String representation for print()
        return f"{self.name}, {self.age}"
    
    def __repr__(self):                  # Official string representation
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):             # Equality (==)
        return self.age == other.age
    
    def __lt__(self, other):             # Less than (<)
        return self.age < other.age
    
    def __len__(self):                   # len()
        return self.age
    
    def __add__(self, years):            # Addition (+)
        return Person(self.name, self.age + years)
    
    def __call__(self):                  # Make object callable
        return f"{self.name} is now callable"
    
    def __del__(self):                   # Destructor
        print(f"Deleting {self.name}")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1)              # __str__: Alice, 25
print(repr(p1))        # __repr__: Person('Alice', 25)
print(p1 == p2)        # __eq__: False
print(p1 < p2)         # __lt__: True
print(len(p1))         # __len__: 25
print(p1 + 5)          # __add__: Alice, 30
print(p1())            # __call__: Alice is now callable
```

**Other Important Dunder Methods:**

```python
# Container operations
__getitem__(self, key)      # obj[key]
__setitem__(self, key, val) # obj[key] = val
__delitem__(self, key)      # del obj[key]
__contains__(self, item)    # item in obj
__iter__(self)              # for loop
__next__(self)              # next()

# Context managers
__enter__(self)             # with statement (entry)
__exit__(self, ...)         # with statement (exit)

# Attribute access
__getattr__(self, name)     # obj.attr (if not found)
__setattr__(self, name, val)# obj.attr = val
__delattr__(self, name)     # del obj.attr
__getattribute__(self, name)# All attribute access
```

---

### Q19: Static Methods vs Class Methods vs Instance Methods

**Answer:**

| Type | Receives | Modifies | Use Case |
|------|----------|----------|----------|
| **Instance Method** | `self` | Instance data | Normal methods |
| **Class Method** | `cls` | Class data | Factory methods, class operations |
| **Static Method** | Neither | Nothing | Utility functions |

**Example:**

```python
class Account:
    interest_rate = 0.05  # Class variable
    
    def __init__(self, balance):
        self.balance = balance  # Instance variable
    
    # Instance Method
    def deposit(self, amount):
        self.balance += amount  # Modifies instance
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    # Class Method
    @classmethod
    def create_with_interest(cls, initial_balance):
        # Factory method - creates instance
        account = cls(initial_balance)
        account.balance *= (1 + cls.interest_rate)
        return account
    
    # Static Method
    @staticmethod
    def calculate_compound_interest(principal, rate, time):
        # Utility function - doesn't need self or cls
        return principal * ((1 + rate) ** time)

# Usage
acc1 = Account(1000)
print(acc1.deposit(500))  # Instance method

acc2 = Account.create_with_interest(1000)  # Class method
print(acc2.balance)  # 1050

interest = Account.calculate_compound_interest(1000, 0.05, 5)  # Static method
print(interest)  # 1276.28
```

---

### Q20: Mixins and Multiple Inheritance

**Answer:**
Mixins are classes that provide additional functionality through multiple inheritance.

**Characteristics:**
- Small, focused classes
- Don't stand alone
- Use cooperative super()
- Provide reusable functionality

**Example:**

```python
# Mixins
class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class ValidatorMixin:
    def validate(self):
        return True

# Base class
class User:
    def __init__(self, name):
        self.name = name

# Combining with Mixins
class LoggedUser(LoggingMixin, User):
    pass

class TimestampedLoggedUser(TimestampMixin, LoggingMixin, User):
    pass

# Usage
user = LoggedUser("Alice")
user.log("User created")

ts_user = TimestampedLoggedUser("Bob")
ts_user.log("Timestamped user created")
print(ts_user.created_at)
```

---

## Additional Key Questions

### Q21: SOLID Principles

**Answer:**
SOLID principles are design guidelines for writing maintainable, scalable code.

**S - Single Responsibility Principle**
```python
# ❌ Bad: Multiple responsibilities
class User:
    def save_to_database(self):
        pass
    
    def send_email(self):
        pass
    
    def validate(self):
        pass

# ✅ Good: Single responsibility
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, user):
        pass

class UserValidator:
    def validate(self, user):
        pass
```

**O - Open/Closed Principle**
```python
# ❌ Bad: Need to modify for new shapes
class AreaCalculator:
    def calculate(self, shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        elif isinstance(shape, Square):
            return shape.side ** 2

# ✅ Good: Closed for modification, open for extension
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def area(self):
        return self.side ** 2

class AreaCalculator:
    def calculate(self, shape: Shape):
        return shape.area()  # Works with ANY shape
```

**L - Liskov Substitution Principle**
```python
# ❌ Bad: Bird can't fly (violates LSP)
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

# ✅ Good: Proper hierarchy
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def swim(self):
        return "Swimming"
```

**I - Interface Segregation Principle**
```python
# ❌ Bad: Force implementation of unwanted methods
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        return "Working"
    
    def eat(self):
        pass  # Robots don't eat!

# ✅ Good: Segregated interfaces
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Worker, Eater):
    def work(self):
        return "Working"
    
    def eat(self):
        return "Eating"

class Robot(Worker):
    def work(self):
        return "Working"
```

**D - Dependency Inversion Principle**
```python
# ❌ Bad: Depends on concrete class
class MySQLDatabase:
    def save(self, data):
        pass

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Depends on concrete

# ✅ Good: Depends on abstraction
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        pass

class UserService:
    def __init__(self, db: Database):  # Depends on abstraction
        self.db = db

# Can inject any Database implementation
service = UserService(MySQLDatabase())
```

---

### Q22: What is CRUD operation in OOP context?

**Answer:**
CRUD = Create, Read, Update, Delete

**Example:**
```python
class User:
    users_db = {}  # Simulated database
    
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    # CREATE
    def save(self):
        User.users_db[self.id] = self
        return f"User {self.name} created"
    
    # READ
    @staticmethod
    def find_by_id(user_id):
        return User.users_db.get(user_id)
    
    # UPDATE
    def update(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email
        return f"User updated"
    
    # DELETE
    def delete(self):
        del User.users_db[self.id]
        return f"User {self.name} deleted"

# Usage
user = User(1, "Alice", "alice@example.com")
print(user.save())  # CREATE
print(User.find_by_id(1).name)  # READ
user.update(name="Alice Smith")  # UPDATE
print(user.delete())  # DELETE
```

---

### Q23: What is the difference between == and is?

**Answer:**

| Operator | Compares | Use Case |
|----------|----------|----------|
| `==` | **Value** (uses `__eq__`) | Are objects equivalent? |
| `is` | **Identity** (memory address) | Are objects same? |

**Example:**
```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Alice")
p3 = p1

print(p1 == p2)  # False (different objects, same value)
print(p1 is p2)  # False (different memory addresses)
print(p1 is p3)  # True (same memory address)

# With __eq__ override
class SmartPerson:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name

sp1 = SmartPerson("Alice")
sp2 = SmartPerson("Alice")

print(sp1 == sp2)  # True (overridden __eq__)
print(sp1 is sp2)  # False (different objects)
```

---

### Q24: Exception Handling with Custom Exceptions

**Answer:**
Create custom exceptions for domain-specific errors.

**Example:**
```python
# Custom Exceptions
class InsufficientBalanceError(Exception):
    def __init__(self, balance, requested):
        self.balance = balance
        self.requested = requested
        super().__init__(f"Balance {balance} < Requested {requested}")

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is invalid")

# Using Custom Exceptions
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

class Person:
    def __init__(self, name, age):
        if age < 0 or age > 150:
            raise InvalidAgeError(age)
        self.name = name
        self.age = age

# Exception Handling
try:
    account = BankAccount(100)
    print(account.withdraw(200))
except InsufficientBalanceError as e:
    print(f"Error: {e}")
    print(f"Balance: {e.balance}, Requested: {e.requested}")

try:
    person = Person("Alice", 300)
except InvalidAgeError as e:
    print(f"Error: {e}")
    print(f"Invalid age: {e.age}")
```

---

### Q25: Design Patterns in OOP

**Answer:**
Design patterns are reusable solutions to common problems.

**Common Patterns:**

**1. Singleton Pattern**
```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()
print(db1 is db2)  # True (same instance)
```

**2. Factory Pattern**
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

dog = AnimalFactory.create_animal("dog")
```

**3. Observer Pattern**
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello!")  # Both observers notified
```

---

# SYSTEM DESIGN EXAMPLES

## Example 1: E-Commerce System

```python
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

# Abstraction
class PaymentMethod(ABC):
    @abstractmethod
    def validate(self):
        pass
    
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(PaymentMethod):
    def validate(self):
        return True
    
    def process(self, amount):
        return f"Charged ${amount} to credit card"

class PayPal(PaymentMethod):
    def validate(self):
        return True
    
    def process(self, amount):
        return f"Charged ${amount} via PayPal"

# Encapsulation
class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
    
    @property
    def price(self):
        return self.__price

class ShoppingCart:
    def __init__(self):
        self.__items = []
    
    def add_item(self, product, quantity):
        self.__items.append({"product": product, "quantity": quantity})
    
    def get_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.__items)

# Inheritance & Polymorphism
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Customer(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.cart = ShoppingCart()
        self.orders = []

class Admin(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
    
    def add_product(self, product):
        return f"Added {product._Product__name}"

# Order Management
class Order:
    def __init__(self, id, customer, payment_method):
        self.id = id
        self.customer = customer
        self.payment_method = payment_method
        self.status = OrderStatus.PENDING
        self.created_at = datetime.now()
    
    def confirm(self):
        self.status = OrderStatus.CONFIRMED
        return "Order confirmed"
    
    def process_payment(self, amount):
        return self.payment_method.process(amount)

# Usage
customer = Customer(1, "Alice", "alice@example.com")
product = Product(1, "Laptop", 999.99)
customer.cart.add_item(product, 1)

payment = CreditCard()
order = Order(1, customer, payment)
print(order.process_payment(customer.cart.get_total()))
print(order.confirm())
```

---

## Example 2: School Management System

```python
from abc import ABC, abstractmethod
from datetime import datetime

class User(ABC):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = datetime.now()
    
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def get_permissions(self):
        pass

class Student(User):
    def __init__(self, id, name, email, student_id, grade):
        super().__init__(id, name, email)
        self.student_id = student_id
        self.grade = grade
        self.courses = []
        self.grades = {}
    
    def get_role(self):
        return "Student"
    
    def get_permissions(self):
        return ["view_grades", "view_courses", "submit_assignment"]
    
    def enroll_course(self, course):
        self.courses.append(course)
    
    def get_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

class Teacher(User):
    def __init__(self, id, name, email, department, salary):
        super().__init__(id, name, email)
        self.department = department
        self.salary = salary
        self.courses = []
    
    def get_role(self):
        return "Teacher"
    
    def get_permissions(self):
        return ["grade_students", "create_assignments", "manage_course"]
    
    def calculate_bonus(self):
        base_bonus = self.salary * 0.10
        course_bonus = len(self.courses) * self.salary * 0.02
        return base_bonus + course_bonus

class Admin(User):
    def __init__(self, id, name, email, access_level):
        super().__init__(id, name, email)
        self.access_level = access_level
    
    def get_role(self):
        return "Admin"
    
    def get_permissions(self):
        return ["manage_users", "generate_reports", "system_settings"]

class Course:
    def __init__(self, course_id, name, teacher):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        student.enroll_course(self)

# Usage
teacher = Teacher(1, "Dr. Smith", "smith@school.edu", "CS", 60000)
student1 = Student(2, "Alice", "alice@school.edu", "S001", "10")
student2 = Student(3, "Bob", "bob@school.edu", "S002", "10")

course = Course(1, "Python 101", teacher)
course.add_student(student1)
course.add_student(student2)
teacher.courses.append(course)

print(f"Teacher: {teacher.name}, Bonus: ${teacher.calculate_bonus()}")
print(f"Course: {course.name}, Students: {len(course.students)}")
```

---

## Summary Checklist

### After Learning This Module, You Should Understand:

- [ ] The four pillars of OOP (E, A, I, P)
- [ ] Classes vs Objects
- [ ] Encapsulation and its benefits
- [ ] Public, protected, private access levels
- [ ] Properties and getters/setters
- [ ] Inheritance and its types
- [ ] super() and MRO
- [ ] Polymorphism and its forms
- [ ] Abstraction and Abstract Base Classes
- [ ] Composition vs Inheritance
- [ ] Dunder methods and their uses
- [ ] Static, class, and instance methods
- [ ] Multiple inheritance and diamond problem
- [ ] Mixins and their use cases
- [ ] SOLID principles
- [ ] Exception handling with custom exceptions
- [ ] Common design patterns (Singleton, Factory, Observer)

### Interview Readiness:

✅ Can explain OOP concepts clearly
✅ Can write clean, well-designed code
✅ Can discuss trade-offs (inheritance vs composition)
✅ Can solve complex object-oriented problems
✅ Can apply SOLID principles
✅ Understand real-world applications
✅ Ready for technical interviews!

---

**Total Coverage: 25 In-Depth Interview Questions + Complete Theory + Real-World Examples**

