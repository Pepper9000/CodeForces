n = int(input())
a = sorted(list(map(int, input().split())))
money = 0
for i in a[:n-1]:
    if i != max(a):
        money += max(a) - i
    else:
        break
print(money)