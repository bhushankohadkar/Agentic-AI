# OOP Quick Reference Cheat Sheet

## FOUR PILLARS OF OOP

### 1. ENCAPSULATION (Data Hiding)
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
```
✅ Benefits: Data protection, validation, flexibility
📌 Access: `self` (public), `_self` (protected), `__self` (private)

### 2. ABSTRACTION (Hide Complexity)
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```
✅ Benefits: Simplify interface, hide details
📌 Use: Abstract Base Classes (ABC)

### 3. INHERITANCE (Code Reuse)
```python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```
✅ Benefits: Code reuse, hierarchy, maintainability
📌 Types: Single, Multi-level, Multiple, Hierarchical, Hybrid

### 4. POLYMORPHISM (Many Forms)
```python
def make_sound(animal: Animal):
    print(animal.speak())  # Works with ANY Animal

make_sound(Dog())   # Woof!
make_sound(Cat())   # Meow!
```
✅ Benefits: Flexibility, extensibility
📌 Types: Compile-time, Runtime, Duck typing, Operator overloading

---

## ACCESS MODIFIERS

```
┌─────────────┬────────┬──────────────┬─────────────┐
│ Level       │ Symbol │ Class        │ Subclass    │
├─────────────┼────────┼──────────────┼─────────────┤
│ Public      │ name   │ ✅ Access    │ ✅ Access   │
│ Protected   │ _name  │ ✅ Access    │ ✅ Access   │
│ Private     │ __name │ ✅ Access    │ ❌ Block    │
└─────────────┴────────┴──────────────┴─────────────┘
```

---

## CLASS VS OBJECT

```python
class Dog:              # Class = Blueprint
    pass

buddy = Dog()          # Object = Instance
max = Dog()            # Another instance
```

**Class**: Template (defined once)
**Object**: Instance (can create many)

---

## super() - PARENT METHOD CALLING

```python
class Parent:
    def method(self):
        return "Parent"

class Child(Parent):
    def __init__(self):
        super().__init__()      # Call parent init
    
    def method(self):
        return super().method() + " + Child"
```

✅ Use for: Initialization, extending methods, MRO
⚠️  Always use instead of `Parent.method(self)`

---

## METHOD RESOLUTION ORDER (MRO)

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())  # [D, B, C, A, object]
```

**Rules:**
1. Child before parent
2. Order of inheritance preserved
3. Each class once (C3 Linearization)

---

## INHERITANCE TYPES

| Type | Example |
|------|---------|
| **Single** | `class Dog(Animal):` |
| **Multi-level** | `class Puppy(Dog):` |
| **Multiple** | `class Duck(Flyable, Swimmer):` |
| **Hierarchical** | `Dog`, `Cat` both inherit from `Animal` |
| **Hybrid** | Mix of above |

---

## COMPOSITION VS INHERITANCE

```python
# Inheritance (IS-A)
class Car(Vehicle):      # Car IS-A Vehicle
    pass

# Composition (HAS-A)
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
```

**Choose Inheritance when:** Clear IS-A, hierarchy ≤ 3 levels
**Choose Composition when:** HAS-A, runtime change, flexibility needed

---

## POLYMORPHISM TYPES

### 1. Method Overriding (Runtime)
```python
class Dog(Animal):
    def speak(self):
        return "Woof!"
```

### 2. Method Overloading (Simulated)
```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc.add(1, 2)      # 3
calc.add(1, 2, 3)   # 6
```

### 3. Duck Typing
```python
def fly(entity):
    return entity.fly()  # No inheritance needed
```

### 4. Operator Overloading
```python
class Vector:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v = v1 + v2  # Uses __add__
```

---

## METHOD TYPES

```python
class Account:
    interest_rate = 0.05  # Class variable
    
    def __init__(self, balance):
        self.balance = balance  # Instance variable
    
    # Instance Method: Operates on THIS object
    def deposit(self, amount):
        self.balance += amount
    
    # Class Method: Operates on CLASS (uses cls)
    @classmethod
    def from_string(cls, data):
        return cls(float(data))
    
    # Static Method: Utility (no self/cls)
    @staticmethod
    def validate(amount):
        return amount > 0
```

---

## PROPERTIES & DECORATORS

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):              # Getter
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):       # Setter
        if value > -273.15:
            self._celsius = value
    
    @property
    def fahrenheit(self):           # Computed property
        return (self._celsius * 9/5) + 32

temp = Temperature(0)
print(temp.celsius)      # 0 (getter)
temp.celsius = 100       # (setter)
print(temp.fahrenheit)   # 212
```

---

## DUNDER METHODS

```python
class Person:
    def __init__(self, name):           # Constructor
        self.name = name
    
    def __str__(self):                  # print()
        return self.name
    
    def __repr__(self):                 # repr()
        return f"Person('{self.name}')"
    
    def __eq__(self, other):            # ==
        return self.name == other.name
    
    def __lt__(self, other):            # <
        return len(self.name) < len(other.name)
    
    def __add__(self, other):           # +
        return Person(self.name + other.name)
    
    def __len__(self):                  # len()
        return len(self.name)
    
    def __getitem__(self, index):       # obj[index]
        return self.name[index]
    
    def __call__(self):                 # obj()
        return f"{self.name} called"
    
    def __del__(self):                  # Destructor
        print(f"Deleting {self.name}")
```

---

## ABSTRACT CLASS VS INTERFACE

```python
# Abstract Class (can have implementation)
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Concrete method
    
    @abstractmethod
    def speak(self):      # Abstract method
        pass

# Interface-like (all abstract)
class Drawable(ABC):
    @abstractmethod
    def draw(self): pass
    
    @abstractmethod
    def get_color(self): pass
```

---

## MIXINS

```python
class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class LoggingMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")

class User:
    def __init__(self, name):
        self.name = name

class FullUser(TimestampMixin, LoggingMixin, User):
    pass

user = FullUser("Alice")
user.log("Created")
```

---

## CUSTOM EXCEPTIONS

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, requested):
        self.balance = balance
        self.requested = requested
        super().__init__(f"Balance {balance} < {requested}")

class BankAccount:
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(f"Error: {e.balance} < {e.requested}")
```

---

## SOLID PRINCIPLES QUICK GUIDE

### S - Single Responsibility
```python
# ❌ User does everything
class User:
    def save(self): pass
    def send_email(self): pass

# ✅ Each class has one job
class User: pass
class UserRepository: pass
class EmailService: pass
```

### O - Open/Closed
```python
# ✅ Open for extension, closed for modification
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * self.r ** 2  # Add new class, don't modify Shape
```

### L - Liskov Substitution
```python
# ✅ Subclass can replace parent
class Bird:
    def move(self): pass

class FlyingBird(Bird):
    def fly(self): pass

class Penguin(Bird):  # Doesn't inherit from FlyingBird (good!)
    def swim(self): pass
```

### I - Interface Segregation
```python
# ❌ Fat interface
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass

# ✅ Separated interfaces
class Worker(ABC):
    @abstractmethod
    def work(self): pass

class Eater(ABC):
    @abstractmethod
    def eat(self): pass
```

### D - Dependency Inversion
```python
# ✅ Depend on abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data): pass

class UserService:
    def __init__(self, db: Database):  # Abstract, not concrete
        self.db = db
```

---

## DESIGN PATTERNS

### Singleton (Single Instance)
```python
class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory (Create Objects)
```python
class PaymentFactory:
    @staticmethod
    def create(payment_type):
        if payment_type == "card":
            return CreditCard()
        elif payment_type == "paypal":
            return PayPal()
```

### Observer (Notify Changes)
```python
class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
```

---

## COMMON MISTAKES

❌ **Using inheritance when composition fits**
```python
class Car(Engine):  # WRONG!
    pass
```

❌ **Deep inheritance hierarchies**
```python
A → B → C → D → E  # Too deep!
```

❌ **Not using super()**
```python
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)  # Use super() instead!
```

❌ **Ignoring MRO in multiple inheritance**
```python
class D(B, C):
    pass  # Always check D.mro()
```

❌ **Breaking encapsulation**
```python
account.__balance = 1000  # Direct access to private
```

---

## == vs is

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (same value)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)
```

---

## WHEN TO USE WHAT

| Need | Use |
|------|-----|
| Blueprint for objects | **Class** |
| Single instance needed | **Singleton** |
| Create objects flexibly | **Factory** |
| Hide internal state | **Encapsulation** |
| Simplify complex interface | **Abstraction** |
| Share common code | **Inheritance** |
| Same method, different behavior | **Polymorphism** |
| Utility functions | **Static methods** |
| Operate on class | **Class methods** |
| Multiple unrelated behaviors | **Mixins** |
| Flexible runtime behavior | **Composition** |

---

## INHERITANCE DECISION TREE

```
Is it IS-A?
├─ YES
│  ├─ Single parent? → Use Inheritance
│  ├─ Multiple parents?
│  │  ├─ Unrelated behaviors? → Use Mixins
│  │  └─ Clear hierarchy? → Use Multiple Inheritance
│  └─ Hierarchy > 3 levels? → Reconsider (use composition)
│
└─ NO (HAS-A)
   ├─ Behavior changes at runtime? → Composition
   ├─ Need flexibility? → Composition
   └─ Static component? → Either (prefer composition)
```

---

## INTERVIEW QUICK REVIEW

**Before Interview, Know:**
- ✅ Four pillars cold
- ✅ Inheritance vs Composition
- ✅ MRO and super()
- ✅ SOLID principles
- ✅ Design patterns
- ✅ When to use each concept

**During Interview:**
- ✅ Think aloud
- ✅ Ask clarifying questions
- ✅ Provide code examples
- ✅ Discuss trade-offs
- ✅ Test your code

**Red Flags:**
- ❌ Can't explain why you used a pattern
- ❌ Code without comments
- ❌ No edge case handling
- ❌ Deep hierarchies justified
- ❌ No testing examples

---

## CODE TEMPLATES

**Class Template**
```python
class ClassName:
    def __init__(self, param):
        self._param = param
    
    def public_method(self):
        pass
    
    @property
    def computed_property(self):
        return self._param
```

**Abstract Class Template**
```python
from abc import ABC, abstractmethod

class AbstractBase(ABC):
    @abstractmethod
    def required_method(self):
        pass
    
    def optional_method(self):
        pass
```

**Inheritance Template**
```python
class Parent:
    def __init__(self, value):
        self.value = value
    
    def method(self):
        return "Parent"

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra
    
    def method(self):
        return super().method() + " + Child"
```

---

**Save this cheat sheet for quick reference during interview prep!** 📝

