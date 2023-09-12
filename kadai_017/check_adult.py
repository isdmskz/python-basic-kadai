class Human:

  def __init__(self, name="", age=""):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
        print(self.name+"さんは大人です。")
    else:
        print(self.name+"さんは大人ではありません。")


a = Human("一郎", 24)
b = Human("二郎", 22)
c = Human("三郎",20)
d = Human("四郎",18)
e = Human("五郎",16)


lst = [a, b, c, d, e]

for i in range(len(lst)):
    lst[i].check_adult()