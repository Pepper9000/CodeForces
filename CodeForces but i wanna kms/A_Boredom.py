input()
a = sorted(list(map(int, input().split())), reverse = True)
b = sorted(list(set(a)), reverse = True)
c = []
points = 0
for i in b:
    c.append(a.count(i))
for i in c:
    x = c.index(max(c))
    
    if x > 0 and b[x] * max(c) > b[x - 1] * c[x - 1]:
        