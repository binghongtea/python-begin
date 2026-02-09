import math
# 注释
a = 1
b = -5
c = 4

r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(r1,r2)