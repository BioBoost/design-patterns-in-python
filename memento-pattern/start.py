# Consider a really basic calculator which can add and subtract.
# Using the memento pattern we can create a history of our
# calculations and roll-back if needed.

class Calculator:
  __result: float = 0
  __formula: str = "0"     # More of indication

  def add(self, operand: float) -> float:
    self.__result += operand
    self.__formula += " + " + str(operand)
    return self.__result
  
  def subtract(self, operand: float) -> float:
    self.__result -= operand
    self.__formula += " - " + str(operand)
    return self.__result
  
  def clear(self) -> None:
    self.__result = 0
    self.__formula = "0"

  def get_result(self) -> float:
    return self.__result
  
  def get_formula(self) -> str:
    return self.__formula
  


### Some demo

calculator = Calculator()

calculator.add(12)
print(calculator.get_formula(), " = ", calculator.get_result())

calculator.subtract(43)
print(calculator.get_formula(), " = ", calculator.get_result())

calculator.subtract(6)
print(calculator.get_formula(), " = ", calculator.get_result())

calculator.add(78)
print(calculator.get_formula(), " = ", calculator.get_result())