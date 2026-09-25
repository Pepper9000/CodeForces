s, n = map(int, input().split())
list1 = []
dict1 = dict()
dead = False
for i in range(n):
    x, y = map(int, input().split())
    if x not in list1:
        list1.append(x)
        dict1[x] = y
    else:
        dict1[x] += y
list1 = sorted(list1)
for i in list1:
    if s > i:
        s += dict1[i]
    else:
        dead = True
print("NO" if dead else "YES")