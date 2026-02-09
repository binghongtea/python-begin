weather = input("请输入天气（好1、坏2）: ")
busy_index = int(input("请输入繁忙指数(1-100): "))
certain_index = input("老婆是不是一定要出去（是1、否2）: ")

if (weather == "1" and busy_index < 60) or  certain_index == "1":
    print("今天可以出去玩")
else :
    print("今天可以不出去玩")