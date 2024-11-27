# POO

# Pilares da POO são: encapsulamento, herança e polimorfismo

# Classe exemplo
class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def greetings(self):
    return f"Olá, meu nome é {self.name} e eu tenho {self.age} anos."

# Objetos
person1 = Person('Mateus', 24)
message = person1.greetings()
print(message)

person2 = Person(name="Maria", age=57)
message = person2.greetings()
print(message)