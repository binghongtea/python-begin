class Grade:
    """成绩类"""

    def __init__(self):
        self.chinese = 0
        self.math = 0
        self.english = 0


class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grade = Grade()  # 初始化成绩对象

    def setGrade(self):
        type = input("请输入科目类型（1语文、2数学、3英语，退出请按q）：")
        while type != "q":
            grade = input("请输入成绩：")
            match type:  # 使用 match 而不是 switch
                case "1":
                    self.grade.chinese = grade
                case "2":
                    self.grade.math = grade
                case "3":
                    self.grade.english = grade
                case _:  # 默认情况
                    print("输入错误，请输入1、2或3")
            type = input("请输入科目类型（退出请按q）：")
        self.showGrade()

    def showGrade(self):
        print(f'''
        姓名是{self.name}
        考号是{self.id}
        语文成绩是{self.grade.chinese}
        数学成绩是{self.grade.math}
        英语成绩是{self.grade.english}
        ''')


student1 = student("张三", "1001")
student1.setGrade()
