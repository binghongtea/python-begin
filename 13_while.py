user_inputList = []

user_input = input("请输入数字(输入q退出): ")
while user_input != 'q':
    user_inputList.append(float(user_input))
    user_input = input("请输入数字(输入q退出): ")

if len(user_inputList) == 0: # 判断列表是否为空
    print('平均值为0')
else :
    print(sum(user_inputList) / len(user_inputList),'平均值')

print(','.join([str(i) for i in user_inputList]))