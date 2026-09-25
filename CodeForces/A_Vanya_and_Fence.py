n, h = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in a:
    if i > h:
        count += 1
print(len(a) + count)