# Consider a really basic calculator which can add and subtract.
# Using the memento pattern we can create a history of our
# calculations and roll-back if needed.
# Here the pattern is implemented using nested/inner classes
# which is not supported by all programming languages
# If more separation is needed it is probable better to create
# normal class and use interfaces to depend on

from dataclasses import dataclass

# Memento interface
class Snapshot:
  def restore(self):
    """Overrides Snapshot.restore()"""
    pass


# Originator interface
class Originator:
  def save(self) -> Snapshot:
    """Overrides Originator.save()"""
    pass


# Introducing data class here for state to keeps things DRY
@dataclass
class CalculatorState:
  result: float = 0
  formula: str = "0"


# Concrete Snapshot class (Immutable)
class CalculatorSnapshot(Snapshot):

  __state: CalculatorState
  __originator: Originator      # Calculator

  def __init__(self, originator, state) -> None:
    self.__state = state
    self.__originator = originator

  def restore(self) -> None:
    self.__originator.restore_state(self.__state)



# Concrete Originator
class Calculator(Originator):

  __state: CalculatorState

  def __init__(self) -> None:
    self.__state = CalculatorState()
    
  def add(self, operand: float) -> float:
    self.__state.result += operand
    self.__state.formula += " + " + str(operand)
    return self.__state.result
  
  def subtract(self, operand: float) -> float:
    self.__state.result -= operand
    self.__state.formula += " - " + str(operand)
    return self.__state.result
  
  def clear(self) -> None:
    self.__state.result = 0
    self.__state.formula = "0"

  def get_result(self) -> float:
    return self.__state.result
  
  def get_formula(self) -> str:
    return self.__state.formula
  
  def save_state(self) -> CalculatorSnapshot:
    return CalculatorSnapshot(self, CalculatorState(
      self.__state.result,
      self.__state.formula
    ))

  def restore_state(self, state: CalculatorState) -> None:
    print("Restoring")
    self.__state.result = state.result
    self.__state.formula = state.formula
  


# Caretaker class
class History:
  __history: list[Snapshot] = []

  def log_action(self, action: Snapshot) -> None:
    self.__history.append(action)

  def undo_action(self) -> None:
    if len(self.__history) == 0:
      return

    snapshot = self.__history.pop()
    snapshot.restore()


### Some demo

# Calculator and History are loosely coupled.
# Basically this means here we can introduce new Originators
# and store their actions in the same History object

# In real-world application this would be encapsulated
# into another class - probable best using command pattern

calculator = Calculator()
history = History()

history.log_action(calculator.save_state())
calculator.add(12)
print(calculator.get_formula(), " = ", calculator.get_result())

history.log_action(calculator.save_state())
calculator.subtract(43)
print(calculator.get_formula(), " = ", calculator.get_result())

history.log_action(calculator.save_state())
calculator.subtract(6)
print(calculator.get_formula(), " = ", calculator.get_result())

history.log_action(calculator.save_state())
calculator.add(78)
print(calculator.get_formula(), " = ", calculator.get_result())

print("Undo !")
history.undo_action()
print(calculator.get_formula(), " = ", calculator.get_result())

print("Undo !")
history.undo_action()
print(calculator.get_formula(), " = ", calculator.get_result())
