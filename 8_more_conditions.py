# BMI = 体重 / 身高 ** 2

user_weight = float(input("请输入您的体重(kg): "))
user_height = float(input("请输入您的身高(m): "))
user_sex = input("请输入您的性别(男1，女0): ")
user_BMI = user_weight / user_height ** 2
print("BMI:", user_BMI)

# 偏瘦 user_BMI <= 18.5
# 正常 18.5 < user_BMI < 25.0
# 偏胖 25.0 <= user_BMI < 30.0
# 肥胖 user_BMI >= 30.0
sex = None
if user_sex == '1' :
    sex = "男"
    if user_BMI <= 18.5 : 
        print(sex + "偏瘦")
    elif 18.5 < user_BMI < 25.0 :
        print(sex + "正常")
    elif 25.0 <= user_BMI < 30.0 :
        print(sex + "偏胖")
    elif user_BMI >= 30.0 :
        print(sex + "肥胖")
else:
    sex = "女"
    if user_BMI <= 18.5 : 
        print(sex + "偏瘦")
    elif 18.5 < user_BMI < 25.0 :
        print(sex + "正常")
    elif 25.0 <= user_BMI < 30.0 :
        print(sex + "偏胖")
    elif user_BMI >= 30.0 :
        print(sex + "肥胖")