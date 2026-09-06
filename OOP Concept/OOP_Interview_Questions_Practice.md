# OOP Interview Questions Practice Guide

## INTERVIEW DIFFICULTY LEVELS

**Junior Level**: Basic understanding of OOP concepts
**Mid Level**: Can implement OOP principles in real scenarios
**Senior Level**: Deep understanding, trade-offs, design decisions

---

# JUNIOR LEVEL INTERVIEWS (0-2 years)

## Q1: What are the four pillars of OOP?

### Expected Answer:
1. **Encapsulation** - Bundling data and methods, controlling access
2. **Abstraction** - Hiding complexity, showing only essentials
3. **Inheritance** - Code reuse through parent-child relationships
4. **Polymorphism** - Same interface, different implementations

### Code Example:
```python
from abc import ABC, abstractmethod

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

# Abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Inheritance & Polymorphism
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

# Polymorphism in action
def print_area(shape: Shape):
    print(shape.area())

print_area(Circle(5))   # Calls Circle's area()
print_area(Square(4))   # Calls Square's area()
```

### Interviewer Follow-ups:
- "Which pillar is most important?" → Encapsulation (data protection)
- "Can you have inheritance without polymorphism?" → Yes, but limited benefit
- "What does abstraction achieve?" → Simplifies interface, hides complexity

---

## Q2: Explain the difference between class and object

### Expected Answer:
- **Class** = Blueprint/Template (defined once)
- **Object** = Instance of class (can create many)
- Analogy: Class is cookie cutter, object is actual cookie

### Code Example:
```python
# Class = Template
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says Woof!"

# Objects = Instances
buddy = Dog("Buddy")    # Object 1
max = Dog("Max")        # Object 2
rex = Dog("Rex")        # Object 3

print(buddy.bark())  # Buddy says Woof!
print(max.bark())    # Max says Woof!
```

### Key Points:
- Class defines structure and behavior
- Multiple objects can be created from one class
- Each object has its own state (attribute values)

---

## Q3: What is encapsulation? Why is it important?

### Expected Answer:
**Encapsulation** = Bundling data + methods + controlling access

**Why important:**
- **Data Protection** - Prevent unauthorized access
- **Validation** - Control how data is modified
- **Flexibility** - Change implementation without breaking interface
- **Maintainability** - Easier to update code

### Code Example:
```python
class Age:
    def __init__(self, years):
        self.__years = 0
        self.set_age(years)  # Use setter for validation
    
    def get_age(self):
        return self.__years
    
    def set_age(self, years):
        if 0 < years < 150:
            self.__years = years
        else:
            raise ValueError("Invalid age")

age = Age(25)
print(age.get_age())  # 25
age.set_age(200)      # ❌ ValueError
```

### Interviewer Follow-up:
- "What if you need to change validation logic?" → Modify only setter method
- "Can someone modify `__years` directly?" → No, private attribute

---

## Q4: What is inheritance and why use it?

### Expected Answer:
**Inheritance** = Child class inherits from parent class

**Why use:**
- **Code Reuse** - Write common code once
- **Hierarchy** - Model real-world relationships
- **Maintainability** - Update common code in one place
- **Extensibility** - Add new features through subclassing

### Code Example:
```python
# Without Inheritance (Bad)
class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Engine started")

class Truck:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Engine started")

# With Inheritance (Good)
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

## Q5: Explain polymorphism with an example

### Expected Answer:
**Polymorphism** = "Many forms" - same method, different behavior

### Code Example:
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Polymorphic function
def make_sound(animal: Animal):
    print(animal.speak())  # Works with ANY Animal subclass

# Same function, different behavior
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    make_sound(animal)
```

---

## Q6: What are public, protected, and private attributes?

### Expected Answer:

| Access Level | Symbol | Accessible From | Use |
|------------|--------|-----------------|-----|
| **Public** | `name` | Anywhere | Public interface |
| **Protected** | `_name` | Class + Subclass | Internal use |
| **Private** | `__name` | Class only | Sensitive data |

### Code Example:
```python
class Person:
    def __init__(self, name, age, ssn):
        self.name = name              # Public
        self._age = age               # Protected
        self.__ssn = ssn              # Private
    
    def get_ssn(self):
        return self.__ssn

person = Person("Alice", 25, "123-45-6789")
print(person.name)           # ✅ OK (public)
print(person._age)           # ✅ Works but not recommended
print(person.__ssn)          # ❌ AttributeError
print(person.get_ssn())      # ✅ OK (through method)
```

---

## Q7: What is super()? When to use it?

### Expected Answer:
`super()` = Call parent class method from child class

**When to use:**
- Initialize parent class in child's `__init__`
- Extend parent method functionality
- Multiple inheritance with proper MRO

### Code Example:
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

---

## Q8: Difference between method overriding and overloading?

### Expected Answer:

| Aspect | Overriding | Overloading |
|--------|-----------|------------|
| **What** | Child redefines parent method | Same method, different params |
| **Python Support** | Yes, native | No, must simulate |
| **How** | Inheritance | `*args`, `**kwargs` |

### Code Example:
```python
# Overriding
class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):  # Override
        return "Woof!"

# Overloading (Simulated)
class Calculator:
    def add(self, *args):  # Variable arguments
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))      # 3
print(calc.add(1, 2, 3))   # 6
```

---

## Q9: What is an abstract class?

### Expected Answer:
Abstract class cannot be instantiated. Forces subclasses to implement specific methods.

### Code Example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# ❌ Cannot instantiate
# animal = Animal()  # TypeError

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "Running"

# ✅ Can instantiate
dog = Dog()
```

---

## Q10: What is the difference between == and is?

### Expected Answer:

| Operator | Compares | Example |
|----------|----------|---------|
| `==` | Value (uses `__eq__`) | Are they equal? |
| `is` | Identity (memory address) | Are they same? |

### Code Example:
```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Alice")
p3 = p1

print(p1 == p2)  # False (different objects)
print(p1 is p2)  # False (different memory)
print(p1 is p3)  # True (same object)

# With __eq__ override
class SmartPerson:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return self.name == other.name

sp1 = SmartPerson("Alice")
sp2 = SmartPerson("Alice")

print(sp1 == sp2)  # True (same value)
print(sp1 is sp2)  # False (different objects)
```

---

# MID LEVEL INTERVIEWS (2-5 years)

## Q11: Explain inheritance types with examples

### Expected Answer:
Five types of inheritance with increasing complexity

### Code Example:
```python
# 1. Single Inheritance
class Animal:
    pass

class Dog(Animal):
    pass

# 2. Multi-level Inheritance
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# 3. Multiple Inheritance
class Flyable:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmer):
    pass

# 4. Hierarchical Inheritance
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 5. Hybrid Inheritance
class Base:
    pass

class Middle(Base):
    pass

class Flyer:
    pass

class Final(Middle, Flyer):
    pass
```

### Interview Follow-ups:
- "When should you use multiple inheritance?" → Use mixins
- "What's the danger?" → Diamond problem
- "How does Python handle it?" → MRO (Method Resolution Order)

---

## Q12: What is Method Resolution Order (MRO)?

### Expected Answer:
MRO is the order Python searches for methods in multiple inheritance.

**Rules:**
1. Child classes before parents
2. Order of inheritance preserved
3. Each class appears once (C3 Linearization)

### Code Example:
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

# View MRO visually
for cls in D.__mro__:
    print(cls)
```

### Follow-up:
"How do you avoid diamond problem?" → Use cooperative super()

```python
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

D()
# Output: A, C, B, D (follows MRO)
```

---

## Q13: Composition vs Inheritance - when to use each?

### Expected Answer:

| Composition (HAS-A) | Inheritance (IS-A) |
|-------------------|------------------|
| Loose coupling | Tight coupling |
| Flexible, runtime change | Fixed at compile time |
| Many levels possible | 2-3 levels max |
| "Uses a" | "Is a" |

### Code Example:
```python
# ❌ Bad: Wrong inheritance
class Engine:
    def start(self):
        return "Engine started"

class Car(Engine):  # Car should NOT inherit from Engine
    pass

# ✅ Good: Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        return self.engine.start()

# When to use inheritance:
class Vehicle:
    pass

class Car(Vehicle):  # Car IS-A Vehicle ✅
    pass

class Truck(Vehicle):  # Truck IS-A Vehicle ✅
    pass
```

### Key Questions to Ask:
1. "Is this an IS-A relationship?" → Use inheritance
2. "Can behavior change at runtime?" → Use composition
3. "Will hierarchy be deep?" → Use composition

---

## Q14: What are dunder methods? Provide examples.

### Expected Answer:
Dunder methods (double underscore) are special methods Python calls for specific operations.

### Code Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):  # print() representation
        return f"{self.name}, {self.age}"
    
    def __repr__(self):  # Official representation
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):  # Equality (==)
        return self.age == other.age
    
    def __lt__(self, other):  # Less than (<)
        return self.age < other.age
    
    def __add__(self, years):  # Addition (+)
        return Person(self.name, self.age + years)
    
    def __len__(self):  # len()
        return self.age
    
    def __call__(self):  # Make callable
        return f"{self.name} is callable"

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1)              # __str__: Alice, 25
print(repr(p1))        # __repr__: Person('Alice', 25)
print(p1 == p2)        # __eq__: False
print(p1 < p2)         # __lt__: True
print(len(p1))         # __len__: 25
print(p1 + 5)          # __add__: Person('Alice', 30)
print(p1())            # __call__: Alice is callable
```

---

## Q15: Instance, Class, and Static Methods - Differences?

### Expected Answer:

| Method | Receives | Modifies | Use Case |
|--------|----------|----------|----------|
| **Instance** | `self` | Instance data | Normal methods |
| **Class** | `cls` | Class data | Factories, class operations |
| **Static** | Neither | Nothing | Utility functions |

### Code Example:
```python
class Account:
    interest_rate = 0.05  # Class variable
    
    def __init__(self, balance):
        self.balance = balance  # Instance variable
    
    # Instance Method
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    # Class Method
    @classmethod
    def create_with_interest(cls, balance):
        account = cls(balance)
        account.balance *= (1 + cls.interest_rate)
        return account
    
    # Static Method
    @staticmethod
    def validate_balance(amount):
        return amount > 0

# Usage
acc1 = Account(1000)
print(acc1.deposit(500))  # Instance: 1500

acc2 = Account.create_with_interest(1000)  # Class method
print(acc2.balance)  # 1050

print(Account.validate_balance(100))  # Static: True
```

---

## Q16: Diamond Problem and its solution

### Expected Answer:
Diamond problem occurs with multiple inheritance when class structure has multiple paths to same parent.

### Code Example:
```python
# The Problem
class A:
    def method(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Question: Which A.method() does D use?
# Answer: Python uses MRO (D → B → C → A)
D().method()  # Output: A

# Solution: Use super()
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
```

---

## Q17: Static vs Class vs Instance - When to use each?

### Expected Answer:
```python
class User:
    total_users = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        User.total_users += 1
    
    # Instance: Operate on this specific instance
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    # Class: Operate on class data or create instances
    @classmethod
    def from_string(cls, user_string):
        name = user_string.split("_")[0]
        return cls(name)
    
    # Static: Utility functions, no access to self/cls
    @staticmethod
    def validate_name(name):
        return len(name) > 2 and name.isalpha()
    
    # Class: Access class variables
    @classmethod
    def get_total_users(cls):
        return cls.total_users

# Usage
print(User.validate_name("Alice"))  # Static method
user = User("Alice")
print(user.greet())  # Instance method
user2 = User.from_string("Bob_Smith")  # Class method
print(User.get_total_users())  # 2
```

---

## Q18: Properties and decorators

### Expected Answer:
Properties allow method calls to look like attribute access.

### Code Example:
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
            raise ValueError("Below absolute zero")
        self._celsius = value
    
    @property
    def kelvin(self):
        """Read-only property"""
        return self._celsius + 273.15

temp = Temperature(0)
print(temp.celsius)     # 0 (getter)
print(temp.fahrenheit)  # 32.0 (computed)
temp.celsius = 100      # setter
print(temp.celsius)     # 100
print(temp.kelvin)      # 373.15 (read-only)
```

---

## Q19: Mixins and Multiple Inheritance

### Expected Answer:
Mixins provide reusable functionality through multiple inheritance.

### Code Example:
```python
# Mixins
class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class ValidatorMixin:
    def validate(self):
        return True

# Base class
class User:
    def __init__(self, name):
        self.name = name

# Combining mixins
class LoggedUser(LoggingMixin, User):
    pass

class FullUser(TimestampMixin, LoggingMixin, User):
    pass

# Usage
user = FullUser("Alice")
user.log("User created")
print(user.created_at)
```

---

## Q20: Custom Exceptions

### Expected Answer:
Create custom exceptions for domain-specific errors.

### Code Example:
```python
# Custom Exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance, requested):
        self.balance = balance
        self.requested = requested
        super().__init__(f"Insufficient funds: {balance} < {requested}")

class InvalidAgeError(Exception):
    pass

# Using them
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

class Person:
    def __init__(self, age):
        if not (0 < age < 150):
            raise InvalidAgeError(f"Invalid age: {age}")
        self.age = age

# Exception handling
try:
    acc = BankAccount(100)
    acc.withdraw(200)
except InsufficientFundsError as e:
    print(f"Error: {e.balance} < {e.requested}")

try:
    person = Person(300)
except InvalidAgeError as e:
    print(f"Error: {e}")
```

---

# SENIOR LEVEL INTERVIEWS (5+ years)

## Q21: SOLID Principles - Explain with code

### Expected Answer:
SOLID = 5 principles for maintainable, scalable code

### Code Example:

**S - Single Responsibility**
```python
# ❌ Bad
class User:
    def save(self): pass
    def send_email(self): pass
    def validate(self): pass

# ✅ Good
class User:
    def __init__(self, name): self.name = name

class UserRepository:
    def save(self, user): pass

class EmailService:
    def send(self, user): pass
```

**O - Open/Closed**
```python
# ❌ Bad: Must modify for each shape
class AreaCalculator:
    def calculate(self, shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.r ** 2
        elif isinstance(shape, Square):
            return shape.s ** 2

# ✅ Good: Open for extension, closed for modification
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * self.r ** 2

class Square(Shape):
    def area(self): return self.s ** 2
```

**L - Liskov Substitution**
```python
# ❌ Bad: Penguin violates Bird contract
class Bird:
    def fly(self): pass

class Penguin(Bird):
    def fly(self): raise Exception("Can't fly")

# ✅ Good: Proper hierarchy
class Bird:
    def move(self): pass

class FlyingBird(Bird):
    def fly(self): pass

class Penguin(Bird):
    def swim(self): pass
```

**I - Interface Segregation**
```python
# ❌ Bad: Force implementation of unwanted methods
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass

class Robot(Worker):
    def work(self): return "Working"
    def eat(self): pass  # Robots don't eat!

# ✅ Good: Segregated interfaces
class Worker(ABC):
    @abstractmethod
    def work(self): pass

class Eater(ABC):
    @abstractmethod
    def eat(self): pass

class Human(Worker, Eater):
    def work(self): return "Working"
    def eat(self): return "Eating"
```

**D - Dependency Inversion**
```python
# ❌ Bad: Depends on concrete class
class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Concrete dependency

# ✅ Good: Depends on abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data): pass

class UserService:
    def __init__(self, db: Database):  # Abstract dependency
        self.db = db
```

---

## Q22: Design Patterns - Singleton, Factory, Observer

### Expected Answer:

**Singleton Pattern** (Single instance)
```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

**Factory Pattern** (Create objects)
```python
class TransportFactory:
    @staticmethod
    def create(transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "truck":
            return Truck()

car = TransportFactory.create("car")
```

**Observer Pattern** (Notify observers)
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
```

---

## Q23: When to use Inheritance vs Composition?

### Expected Answer:
Decision tree:
```
Is it an IS-A relationship?
├─ Yes → Use Inheritance
│   └─ Is hierarchy ≤ 2-3 levels?
│       ├─ Yes → Inheritance is OK
│       └─ No → Consider composition
└─ No → Use Composition
    └─ Does behavior change at runtime?
        ├─ Yes → Composition is better
        └─ No → Either works (composition preferred)
```

### Real Example:
```python
# ✅ Inheritance: Bird IS-A Animal
class Animal: pass
class Bird(Animal): pass
class Penguin(Bird): pass

# ✅ Composition: Car HAS-A Engine
class Engine: pass
class Car:
    def __init__(self):
        self.engine = Engine()

# ✅ Composition: Employee HAS-A Role (changes at runtime)
class Role(ABC):
    @abstractmethod
    def get_salary_multiplier(self): pass

class Manager(Role):
    def get_salary_multiplier(self): return 1.5

class Developer(Role):
    def get_salary_multiplier(self): return 1.3

class Employee:
    def __init__(self, name, salary, role: Role):
        self.name = name
        self.salary = salary
        self.role = role  # Can change at runtime
    
    def get_total_salary(self):
        return self.salary * self.role.get_salary_multiplier()

emp = Employee("Alice", 5000, Developer())
emp.role = Manager()  # Changed at runtime!
```

---

## Q24: How would you design [Complex System]?

### Expected Answer Pattern:
1. **Identify entities** (classes needed)
2. **Define relationships** (inheritance, composition)
3. **Apply SOLID principles**
4. **Handle edge cases**
5. **Consider scalability**

### Example: Design an E-Commerce System

```python
from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

# Entities
class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

class User(ABC):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    @abstractmethod
    def get_role(self): pass

class Customer(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.cart = ShoppingCart()
        self.orders = []
    
    def get_role(self):
        return "Customer"

class Product:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price
    
    @property
    def price(self):
        return self._price

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount): pass

class CreditCard(PaymentMethod):
    def process(self, amount):
        return f"Charged ${amount}"

class Order:
    def __init__(self, id, customer, payment: PaymentMethod):
        self.id = id
        self.customer = customer
        self.payment = payment
        self.items = []
        self.status = OrderStatus.PENDING
        self.created_at = datetime.now()
    
    def add_item(self, product, quantity):
        self.items.append({"product": product, "qty": quantity})
    
    def get_total(self):
        return sum(item["product"].price * item["qty"] for item in self.items)
    
    def confirm(self):
        result = self.payment.process(self.get_total())
        self.status = OrderStatus.CONFIRMED
        return result

# Usage
customer = Customer(1, "Alice", "alice@example.com")
product = Product(1, "Laptop", 999.99)
customer.cart.items.append(product)

payment = CreditCard()
order = Order(1, customer, payment)
order.add_item(product, 1)
print(order.confirm())
```

---

## Q25: Explain Code That Does [Thing] - Optimization/Refactoring

### Expected Answer:
Interview may show you bad code and ask to refactor it.

### Example:

```python
# ❌ Bad Code (Tight coupling, hard to test)
class UserManager:
    def __init__(self):
        self.db = MySQLDatabase()
    
    def create_user(self, name):
        user = {"name": name, "created": datetime.now()}
        self.db.save(user)
        self.send_email(user)
    
    def send_email(self, user):
        # Email sending logic
        pass

# ✅ Refactored (Loose coupling, testable)
class Database(ABC):
    @abstractmethod
    def save(self, data): pass

class EmailService(ABC):
    @abstractmethod
    def send(self, user): pass

class UserManager:
    def __init__(self, db: Database, email_service: EmailService):
        self.db = db
        self.email_service = email_service
    
    def create_user(self, name):
        user = User(name)
        self.db.save(user)
        self.email_service.send(user)

# Dependency injection makes testing easy
class MockDatabase(Database):
    def save(self, data): pass

class MockEmailService(EmailService):
    def send(self, user): pass

# Test
db = MockDatabase()
email = MockEmailService()
manager = UserManager(db, email)
```

---

# INTERVIEW TIPS

## Before the Interview

- [ ] Review all four pillars
- [ ] Practice writing code for each concept
- [ ] Understand trade-offs (composition vs inheritance)
- [ ] Know design patterns
- [ ] Review SOLID principles
- [ ] Practice system design

## During the Interview

1. **Clarify the question** - "Are you asking about...?"
2. **Think aloud** - Show your reasoning
3. **Provide code examples** - Don't just talk
4. **Discuss trade-offs** - "Pro: X, Con: Y"
5. **Handle follow-ups** - Don't memorize, understand deeply

## Example Interview Flow

```
Interviewer: "Explain inheritance"
You: "Inheritance allows child classes to inherit from parent classes..."
     (Provide simple example)
     
Interviewer: "When would you NOT use inheritance?"
You: "When behavior changes at runtime, composition is better..."
     (Show composition example)
     
Interviewer: "Can you show me how you'd design X?"
You: "Let me think... First, I need to identify entities..."
     (Draw/explain design, then code)
```

## Common Mistakes to Avoid

- ❌ Saying "I don't know" without thinking
- ❌ Providing code without explanation
- ❌ Not asking clarifying questions
- ❌ Over-complicating simple concepts
- ❌ Forgetting edge cases
- ❌ Not testing your code examples

---

## Quick Reference: When to Use What

| Concept | When | Example |
|---------|------|---------|
| **Inheritance** | IS-A relationship, code reuse | Animal → Dog → Puppy |
| **Composition** | HAS-A relationship, runtime flexibility | Car HAS-A Engine |
| **Abstract Classes** | Force implementation of methods | PaymentMethod (credit card, PayPal) |
| **Interfaces** | Define contract for multiple classes | Drawable, Saveable |
| **Encapsulation** | Protect sensitive data | Bank account balance |
| **Polymorphism** | Different behavior, same interface | Shape.area() |
| **Static Methods** | Utility functions | ValidationUtils |
| **Class Methods** | Factory methods, class data | User.from_string() |
| **Mixins** | Reusable functionality | TimestampMixin |

---

## Final Checklist

Before your interview, make sure you can:

- [ ] Explain four pillars in < 2 minutes
- [ ] Provide code examples for all concepts
- [ ] Discuss inheritance vs composition trade-offs
- [ ] Explain MRO and diamond problem
- [ ] Describe SOLID principles
- [ ] Analyze and refactor bad code
- [ ] Design a system with proper OOP
- [ ] Answer follow-up questions comfortably
- [ ] Write bug-free code during interview
- [ ] Discuss your design decisions

**You're ready for your OOP interview!** 🚀

