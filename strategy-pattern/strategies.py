# A better option is to use the strategy pattern

class Rectangle:
  
  __width: int
  __height: int
  __symbol: str = "x"
  __strategy = None   # How can we indicate type here ?

  def __init__(self, width: int, height: int) -> None:
    self.__width = width
    self.__height = height

  def get_width(self) -> int:
    return self.__width
  
  def get_height(self) -> int:
    return self.__height
  
  def get_symbol(self) -> str:
    return self.__symbol
  
  def set_drawing_strategy(self, strategy):
    self.__strategy = strategy
    return self
  
  def draw(self) -> str:
    if (self.__strategy != None):
      return self.__strategy.draw(self)
    else:
      return ""


class DrawingStrategy:

  def draw(self, context: Rectangle) -> str:
    """Overrides DrawingStrategy.draw()"""
    pass


class FilledStrategy(DrawingStrategy):

  def draw(self, context: Rectangle) -> str:
    output: str = "";

    for w in range(context.get_width()):
      for h in range(context.get_height()):
        output += context.get_symbol()
      output += "\n"

    return output


class BorderOnlyStrategy(DrawingStrategy):

  def draw(self, context: Rectangle) -> str:
    output: str = "";

    for w in range(context.get_width()):
      for h in range(context.get_height()):
        if (w == 0 or h == 0 or (w == context.get_width()-1) or (h == context.get_height()-1)):
          output += context.get_symbol()
        else:
          output += " "
      output += "\n"

    return output

class InternalOnlyStrategy(DrawingStrategy):

  def draw(self, context: Rectangle) -> str:
    output: str = "";

    for w in range(context.get_width()):
      for h in range(context.get_height()):
        if (w == 0 or h == 0 or (w == context.get_width()-1) or (h == context.get_height()-1)):
          output += " "
        else:
          output += context.get_symbol()
      output += "\n"

    return output



# Some demo code
rectangle = Rectangle(5, 12)

print(rectangle.set_drawing_strategy(BorderOnlyStrategy()).draw())
print(rectangle.set_drawing_strategy(InternalOnlyStrategy()).draw())
print(rectangle.set_drawing_strategy(FilledStrategy()).draw())