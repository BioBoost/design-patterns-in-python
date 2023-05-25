# Consider an application that can draw a rectangle in different ways
# Each possible option can be found in the Rectangle class.
# However, it's becoming to large and should be refactored

class Rectangle:
  
  __width: int
  __height: int
  __symbol: str = "x"

  def __init__(self, width: int, height: int) -> None:
    self.__width = width
    self.__height = height

  def draw_filled(self) -> str:
    output: str = "";

    for w in range(self.__width):
      for h in range(self.__height):
        output += self.__symbol
      output += "\n"

    return output
        
  def draw_border_only(self) -> str:
    output: str = "";

    for w in range(self.__width):
      for h in range(self.__height):
        if (w == 0 or h == 0 or (w == self.__width-1) or (h == self.__height-1)):
          output += self.__symbol
        else:
          output += " "
      output += "\n"

    return output
        
  def draw_internal_only(self) -> str:
    output: str = "";

    for w in range(self.__width):
      for h in range(self.__height):
        if (w == 0 or h == 0 or (w == self.__width-1) or (h == self.__height-1)):
          output += " "
        else:
          output += self.__symbol
      output += "\n"

    return output


# Some demo code

rectangle = Rectangle(5, 12)

print(rectangle.draw_border_only())
print(rectangle.draw_internal_only())
print(rectangle.draw_filled())