n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
p = [a[0]]
for i in a[1:]:
    p.append(p[-1] + i)
for i in q:
    for j in range(n):
        if p[j] >= i:
            print(j + 1)
            break