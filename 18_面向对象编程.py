class CuteCat:
    def __init__(self, name ,age, color):
        self.name = name
        self.age = age
        self.color = color
    def printInfo(self, master):
        print(f"它是{master}的猫 name:", self.name, "age:", self.age, "color:", self.color, '喵' * self.age)

cat1 = CuteCat("Mimi", 2, "white")
cat1.printInfo('yzk')