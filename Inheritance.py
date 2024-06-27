class Vehicle:
    def __init__(self,color,wheels):
        self.color=color
        self.wheels=wheels
    def description(self):
        return f"This {self.color} vehicle has {self.wheels} wheels."
class Car(Vehicle):
    def __init__(self, color, wheels, doors):
        super().__init__(color, wheels)
        self.doors=doors
    def description(self):
        return f"This {self.color} car has {self.wheels} wheels and {self.doors} doors."
class Motorcycle(Vehicle):
    def __init__(self, color, wheels, engine_size):
        super().__init__(color, wheels)
        self.engine_size=engine_size
    def description(self):
        return f"This {self.color} motorcycle has {self.wheels} wheels and an engine size of {self.engine_size}."
my_car=Car("Red",4,4)
my_motorcycle=Motorcycle("Blue",2,650)
print(my_car.description())    
print(my_motorcycle.description())