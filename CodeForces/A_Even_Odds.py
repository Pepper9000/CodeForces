import math as m 
n, k = map(int, input().split())
print(k*2 -1) if m.ceil(n/2) >= k else print((k-m.ceil(n/2))*2)