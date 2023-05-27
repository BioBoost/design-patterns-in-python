from dataclasses import dataclass
from typing import Any

# Think about an app that keeps track of your contacts
# The contact class does expose some methods only required to loop
# over the contacts.
# Using the iterator pattern we can uniformly implement this.

@dataclass
class User:
  name: str = "Anonymous"
  email: str = "private@example.com"


class Contacts:
  __users: list[User] = []

  def add(self, contact: User) -> None:
    self.__users.append(contact)

  def get_by_index(self, index: int) -> User:
    if (index >= len(self.__users) or index < 0):
      raise IndexError()
    
    return self.__users[index]

  def count(self) -> int:
    return len(self.__users)

  def get_by_email(self, email: str) -> User | None:
    for user in self.__users:
      if user.email == email:
        return user


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
for i in range(0, myContacts.count()):
  print("- ", myContacts.get_by_index(i))
