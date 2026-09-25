n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
money = 0
for i in range(m):
    if x[i] < 0:
        money += x[i]
print(abs(money))