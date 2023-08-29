class Human:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def setinfo(self, name):  # これ必要？
    self.name = name

  def printinfo(self):  # これ必要？
    print(self.name)

ishida = Human("Masa Ishida",48)

print(ishida.name)
print(ishida.age)
