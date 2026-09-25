input()
a = list(map(int, input().split()))
count, counts, x = 1, [], a[0]
for i in range(1, len(a)):
    y = a[i]
    if y >= x:
        count += 1
    elif y < x:
        counts.append(count)
        count = 1
    x = y
counts.append(count)
print(max(counts))