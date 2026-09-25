import math as m
a, *b = (map(int, input().split()))
b = sorted(b)
x = []
if a % b[0] == 0:
    x.append(a // b[0])
if a % b[1] == 0:
    x.append(a // b[1])
if a % b[2] == 0:
    x.append(a // b[2])
print(max(x))