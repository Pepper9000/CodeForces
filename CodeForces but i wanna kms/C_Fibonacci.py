n = int(input())
a = [1, 1]
while len(a) != n:
    a.append(a[-1] + a[-2])
print(a[-1] % (10 ** 9 + 7))