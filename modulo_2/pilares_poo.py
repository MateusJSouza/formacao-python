# Exemplo de herança
print("\nExemplo de herança:")

class Animal:
  def __init__(self, name) -> None:
    self.name = name

  def walk(self):
    print(f"O animal {self.name} andou")
    return

  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    return 'Au, au'

class Cat(Animal):
  def make_sound(self):
    return 'Miau!'