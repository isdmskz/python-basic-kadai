class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def printinfo(self):
    print(self.name)

human = Human("石田正和", 48)

print(human.name)
print(human.age)