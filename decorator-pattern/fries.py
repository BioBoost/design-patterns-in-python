class Product:
  def cost(self) -> int:
    """Overrides Product.cost()"""
    pass

  def description(self) -> str:
    """Overrides Product.description()"""
    pass

class NormalFries(Product):
  def cost(self) -> int:
    return 3
  
  def description(self) -> str:
    return "Normal fries"
  
class LargeFries(Product):
  def cost(self) -> int:
    return 5
  
  def description(self) -> str:
    return "Large fries"
  
class SmallFries(Product):
  def cost(self) -> int:
    return 2
  
  def description(self) -> str:
    return "Small fries"
  

# Base Decorator
class ToppingDecorator(Product):

  __product: Product
  
  def __init__(self, product: Product) -> None:
    self.__product = product

  def cost(self) -> int:
    return self.__product.cost()
  
  def description(self) -> str:
    return self.__product.description()

# Concrete Decorators
class Salt(ToppingDecorator):
  def cost(self) -> int:
    total = ToppingDecorator.cost(self)   # Call parent cost
    return total + 1
  
  def description(self) -> str:
    output = ToppingDecorator.description(self)
    return output + " with salt"
  
class Ketchup(ToppingDecorator):
  def cost(self) -> int:
    total = ToppingDecorator.cost(self)
    return total + 1
  
  def description(self) -> str:
    output = ToppingDecorator.description(self)
    return output + " with ketchup"
  

# Client code

fries = LargeFries()
fries = Salt(fries)
fries = Ketchup(fries)

print("Result: ", fries.description(), " | Cost = ", fries.cost())


fries = SmallFries()
fries = Salt(fries)

print("Result: ", fries.description(), " | Cost = ", fries.cost())