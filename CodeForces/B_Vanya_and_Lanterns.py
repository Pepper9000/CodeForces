n ,l = map(int, input().split())
x = list(map(int, input().split()))
x = sorted(x)
if 0 not in x and l not in x:
    if x[0] > l - x[-1]:
        maxx = x[0] * 2
    else:
        maxx = (l - x[-1]) * 2
elif 0 not in x:
    maxx = x[0] * 2
elif l not in x:
    maxx = (l - x[-1]) * 2
else:
    maxx = 0
for i in range(n-1):
    if x[i + 1] - x[i] > maxx:
        maxx = x[i+1] - x[i]
print(maxx/2)