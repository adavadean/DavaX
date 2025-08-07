# Ex1 Shape area calculator using inheritance and abstract class

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

print(Rectangle.__doc__)
print(Circle.__doc__)

shapes = [
    Rectangle(3, 4),
    Circle(2),
    Rectangle(5, 2),
    Circle(1),
    Rectangle(7, 1)
]

rect_count = 0
circle_count = 0

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
    if isinstance(shape, Rectangle):
        rect_count += 1
    elif isinstance(shape, Circle):
        circle_count += 1

print(f"Rectangles: {rect_count}, Circles: {circle_count}")

# Ex 2 Bank account class with encapsulation and validation

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = 0
        self.balance = initial_balance  # use setter

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

# Test
account = BankAccount(100)
print("Initial balance:", account.balance)
account.deposit(50)
print("After deposit:", account.balance)
account.withdraw(30)
print("After withdrawal:", account.balance)

try:
    account.withdraw(200)
except ValueError as e:
    print("Error:", e)

try:
    account.balance = -500
except ValueError as e:
    print("Error:", e)

# Ex 3 Notification system with polymorphism and duck typing

class EmailNotification:
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMSNotification:
    def send(self, message):
        print(f"Sending SMS: {message}")

def send_bulk(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)

notifier_list = [
    EmailNotification(),
    SMSNotification(),
    EmailNotification()
]

send_bulk(notifier_list, "System maintenance scheduled.")
