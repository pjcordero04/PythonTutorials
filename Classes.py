from abc import ABC, abstractmethod

class Shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This shape is {self.color} and {'filled' if self.is_filled else 'not_filled'}.")
        
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def describe(self):
        super().describe()
        area = self.area()
        circ = self.circumference()
        print(f"This circle has an area of {area} and a circumference of {circ}")
    
class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color,is_filled)
        self.side = side 

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def describe(self):
        area = self.area()
        peri = self.perimeter()
        super().describe()
        print(f"This square has an area of {area} and a perimeter of {peri}")
    

circle = Circle("red", True, 5)
circle.describe()
print("")
print("")
square = Square("Blue", False, 9)
square.describe()


class Animal():
    def __init__(self, name, color,is_domesticated):
        self.name = name
        self.color = color
        self.is_domesticated = is_domesticated

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        print(f"{self.name} the {self.color} {self.__class__.__name__.lower()} is {'domesticated' if self.is_domesticated else 'not domesticated'}.")


class Cat(Animal):

    def eat(self):
        print(f"{self.name} the cat is eating.")

    def move(self):
        print(f"{self.name} the cat is walking.")


class Dog(Animal):

    def eat(self):
        print(f"{self.name} the dog is eating.")

    def move(self):
        print(f"{self.name} the dog is walking.")


cat = Cat("Tom", "gray", True)
dog = Dog("Bella","white",False)
print("")
print("")
cat.eat()
dog.move()
cat.describe()
dog.describe()
