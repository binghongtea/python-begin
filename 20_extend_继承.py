class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def print_info(self):
        print(f'员工姓名：{self.name},员工编号：{self.id}')

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    
    def calculate_monthly_salary(self):
        print(f'{self.name}的工资是{self.monthly_salary}')

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    
    def calculate_monthly_salary(self):
        print(f'{self.name}的工资是{self.daily_salary * self.work_days}')

# 错误：缺少 name 和 id 参数
# FullTimeEmployee(5000)

# 正确的创建方式：
FullTimeEmployee1 = FullTimeEmployee("张三", "001", 5000)
FullTimeEmployee1.calculate_monthly_salary()
FullTimeEmployee1.print_info()

PartTimeEmployee1 = PartTimeEmployee("张三", "001", 500, 20)
PartTimeEmployee1.calculate_monthly_salary()
PartTimeEmployee1.print_info()
