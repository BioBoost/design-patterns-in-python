from dataclasses import dataclass
from typing import Any

# Iterator interface
class Iterator:

  def next(self) -> Any:
    """Overrides the method Iterator.next()"""
    pass

  def has_more(self) -> bool:
    """Overrides the method Iterator.has_more()"""
    pass


# Iterable collection interface
class Iterable:

  def create_iterator(self) -> Iterator:
    """Overrides the method Iterable.create_iterator()"""


# This is the concrete implementation that depends on the
# Contacts
class ForwardContactIterator(Iterator):

  __collection: Any         # Contacts
  __currentIndex: int = 0   # This actually depends on the collection

  def __init__(self, collection):
    self.__collection = collection

  def has_more(self) -> bool:
    return self.__currentIndex < self.__collection.count()

  def next(self) -> Any:
    if self.has_more():
      result = self.__collection.get_by_index(self.__currentIndex)
      self.__currentIndex += 1
      return result
    
    return None



@dataclass
class User:
  name: str = "Anonymous"
  email: str = "private@example.com"


class Contacts(Iterable):
  __users: list[User] = []

  def add(self, contact: User) -> None:
    self.__users.append(contact)

  def get_by_email(self, email: str) -> User | None:
    for user in self.__users:
      if user.email == email:
        return user

  def get_by_index(self, index: int) -> User:
    if (index >= len(self.__users) or index < 0):
      raise IndexError()
    
    return self.__users[index]
  
  def create_iterator(self) -> Iterator:
    return ForwardContactIterator(self)

  def count(self) -> int:
    return len(self.__users)
      



## Some basic demo

myContacts = Contacts()
myContacts.add(User("Nico", "nico@example.com"))
myContacts.add(User("Bart", "bart@example.com"))
myContacts.add(User("Daniel", "daniel@example.com"))

user = myContacts.get_by_email("nico@example.com")
print(user)

empty = myContacts.get_by_email("none@gmail.com")
print(empty)

print("My Contacts")
iterator = myContacts.create_iterator()
while iterator.has_more():
  print("- ", iterator.next())

# Note that we are not depending anymore on the way the contacts are internally stored or have to be accessed.