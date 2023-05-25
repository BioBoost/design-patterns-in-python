# Consider an application that calculates the area and circumference of any shape.
# We have basic shapes like circles, rectangles, triangles, ...
# We also want to have more complex shapes that can be made up of the primitive shapes

import math

class Shape:
  
  def area() -> float:
    """Overrides Shape.area()"""
    pass

  def circumference() -> float:
    """Overrides Shape.circumference()"""


# Circle is a leaf
class Circle(Shape):
  __radius: float

  def __init__(self, radius) -> None:
    self.__radius = radius

  def area(self) -> float:
    return math.pi * self.__radius * self.__radius
  
  def circumference(self) -> float:
    return 2 * math.pi * self.__radius
  
# Rectangle is a leaf
class Rectangle(Shape):
  __width: float
  __height: float

  def __init__(self, width, height) -> None:
    self.__width = width
    self.__height = height

  def area(self) -> float:
    return self.__width * self.__height
  
  def circumference(self) -> float:
    return 2 * (self.__width + self.__height)

# This is the Composite class
class Container(Shape):
  __children: list[Shape]

  def __init__(self) -> None:
    self.__children = []

  def add_child(self, shape: Shape) -> None:
    self.__children.append(shape)

  def area(self) -> float:
    total: float = 0
    for shape in self.__children:
      total += shape.area()
    
    return total

  def circumference(self) -> float:
    total: float = 0
    for shape in self.__children:
      total += shape.circumference()
    
    return total


shapes = Container()
shapes.add_child(Circle(3))
shapes.add_child(Rectangle(2, 3))

container = Container()
container.add_child(Circle(2))
container.add_child(Circle(3))
container.add_child(Circle(4))

shapes.add_child(container)

print("Total Area: ", shapes.area())
print("Total Circumference: ", shapes.circumference())