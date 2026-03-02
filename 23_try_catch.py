try:
    user_weight = float(input("请输入您的体重(kg): "))
    user_height = float(input("请输入您的身高(m): "))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print('请输入数字类型')
except ZeroDivisionError:
    print('请输入非零数字')
except:
    print('发生了未知错误，请重试')
else:
    print('您的BMI为：', user_BMI)
finally:
    print('程序结束')