user_weight = float(input('请输入您的体重(kg): '))
user_height = float(input('请输入您的身高(m): '))

def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        print('偏瘦')
    elif BMI > 18.5 and BMI < 25.0:
        print('正常')
    elif BMI >= 25.0 and BMI < 30.0:
        print('偏胖')
    elif BMI >= 30.0:
        print('肥胖')
    return BMI

user_bmi = calculate_BMI(user_weight, user_height)
print(f'您的bmi为{user_bmi}')