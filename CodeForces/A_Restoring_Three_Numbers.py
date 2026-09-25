a = list(map(int, input().split()))
abc = max(a)
a = sorted(a)
for i in a[:3]:
    print(abc - i, end = " ")