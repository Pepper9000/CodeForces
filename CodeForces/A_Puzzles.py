n, m = map(int, input().split())
x = list(map(int, input().split()))
x = sorted(x)
a = 10**9
for i in range(m-n+1):
    a = min(a, x[i+n-1] - x[i])
print(a)