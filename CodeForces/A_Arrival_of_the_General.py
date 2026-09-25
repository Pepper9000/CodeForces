n = int(input())
a = list(map(int, input().split()))
print(a.index(max(a)) + (n-1 -(n-1-a[::-1].index(min(a)))) - (1 if a.index(max(a))>(n-1-a[::-1].index(min(a))) else 0) )