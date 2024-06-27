# Method Overloading

class Calculator:
    def calculate(self, a, b):
        return a + b

    def calculate(self, a, b, c):
        return a + b + c

    # This will raise a TypeError because Python does not support method overloading
    # Instead, we can use default arguments to achieve similar behavior

class CalculatorFixed:
    def calculate(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

calc = CalculatorFixed()
print(calc.calculate(10, 20))  # Output: 30
print(calc.calculate(10, 20, 30))  # Output: 60

# Method Overriding

class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

dog = Dog()
cat = Cat()

dog.sound()  # Output: The dog barks.
cat.sound()  # Output: The cat meows.

# Polymorphism

def make_sound(animal):
    animal.sound()

make_sound(dog)  # Output: The dog barks.
make_sound(cat)  # Output: The cat meows.