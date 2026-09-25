n, k = map(int, input().split())
l = list(map(int, input().split()))
count = 0
for i in l:
    if i + k <= 5:
        count += 1
print(count // 3)