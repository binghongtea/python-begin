# BMI = 体重 / 身高 ** 2

user_weight = float(input("请输入您的体重(kg): "))
user_height = float(input("请输入您的身高(m): "))
user_BMI = user_weight / user_height ** 2
print("BMI:", user_BMI)
