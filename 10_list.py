itemList = []
itemList.append("鼠标")
itemList.append("键盘")
itemList.remove("鼠标")
itemList.append("屏幕")

print(itemList)
print(len(itemList))

priceList = [888,222,30,2323]

max_price = max(priceList)
min_price = min(priceList)
sum_price = sum(priceList)
sorted_priceList = sorted(priceList)
print(max_price)
print(min_price)
print(sum_price)
print(sorted_priceList)