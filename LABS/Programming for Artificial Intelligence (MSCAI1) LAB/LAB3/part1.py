# OOPs, Concepts and Data Structures in Python

# Class Implementation Türkçe: Sınıf Uygulaması

import math


class Dog:
    """
    A class to represent a dog.
    """

    def __init__(
        self, name, breed
    ):  # self: referans alır, name: köpeğin adı, breed: köpeğin cinsi
        self.name = name  # Name of the dog
        self.breed = breed  # Breed of the dog
        self.energy = 100  # Energy level (0-100)

    def bark(self):
        print(f"{self.name} says Woof!")

    def walk(self):
        if self.energy >= 10:
            self.energy -= 10  # Decrease energy by 10
            print(f"{self.name} is walking.")
        else:
            print(f"{self.name} is too tired to walk.")

    def eat(self, food_amount):
        self.energy += food_amount  # Increase energy by food amount
        if self.energy > 100:
            self.energy = 100  # Energy cannot exceed 100
        print(f"{self.name} ate food. Energy level: {self.energy}")

    def get_energy(self):
        return self.energy  # Return current energy level


# Example usage
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
my_dog.walk()
my_dog.eat(30)


# Exercise 1: Book Class Implementation
class Book:
    """
    A class to represent a book.
    """

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long_read(self):
        """
        Returns True if the book has more than 300 pages.
        """
        return self.pages > 300


# Example usage
book = Book("War and Peace", "Leo Tolstoy", 1225)
print(book.is_long_read())  # True


# Exercise 2: Simple Bank Account Class
class BankAccount:
    """
    A class to represent a bank account.
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Current balance: {self.balance}")

    def account_balance(self):
        return self.balance


# Example usage
account = BankAccount("Alice", 500)
account.deposit(200)
account.withdraw(100)
account.balance  # 600

# Exercise 3: Circle Class


class Circle:
    """
    A class to represent a circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


# Example usage
circle = Circle(5)
print(circle.calculate_area())  # 78.54
print(circle.calculate_circumference())  # 31.42


# Exception Handling Example
def divide(a, b):
    """
    A function to perform division with exception handling.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Unsupported data types. Provide numbers.")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution complete.")


# Example usage
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error: Cannot divide by zero.
print(divide(10, "a"))  # Error: Unsupported data types.

# Linked List Class Implementation


class Node:
    """
    A class to represent a node in a linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class to represent a linked list.
    """

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if not current_node:
                raise IndexError("Position out of range")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if not current_node:
            print("Node not found")
            return
        prev_node.next = current_node.next
        current_node = None

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next  # current_node'u güncelliyoruz
        print("None")


# Example usage
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_position(15, 1)
ll.display()
print(ll.search(20))
ll.delete_node(15)
ll.display()
