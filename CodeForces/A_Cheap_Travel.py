import math
n, m, a, b = map(int, input().split())
print(min(n*a, (n // m) * b + (n - (n // m)*m) * a, math.ceil(n / m) * b))