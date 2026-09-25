import math as m
x = list(map(int, input().split()))
print(m.ceil(x[0] / x[2]) * m.ceil(x[1] / x[2]))