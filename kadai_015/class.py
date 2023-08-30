class Human:

  def __init__(self):
    self.name = ""
    self.age = ""

  def setinfo(self, name, age):
    self.name = name
    self.age = age

  def printinfo(self):
    print(self.name)
    print(self.age)

masa = Human()

masa.setinfo("Masakazu Ishida", 48)
masa.printinfo()
