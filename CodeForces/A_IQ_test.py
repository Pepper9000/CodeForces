n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i % 2 == 0:
        b.append(1)
    elif i % 2 != 0:
        b.append(0)
print(b.index(1)+1 if b.count(1) == 1 else b.index(0)+1)