n, t = map(int, input().split())
a = list(map(int, input().split()))
me = 1
while me < t:
    me += a[me - 1]
if me == t:
    print("YES")
else:
    print("NO")