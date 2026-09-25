tot = 0
total = []
for i in range(int(input())):
    a, b = map(int, input().split())
    tot = tot - a + b
    total.append(tot)
print(max(total))