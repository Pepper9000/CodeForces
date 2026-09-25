n = int(input())
a = list(map(int, input().split()))
count, x = 0, [a[0]]
for i in a[1:]:
    if i > max(x) or i < min(x):
        count += 1
        x.append(i)
print(count)