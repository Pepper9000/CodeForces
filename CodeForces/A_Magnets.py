n = int(input())
a = []
for i in range(n):
    a.append(input())
count = 1
for i in range(n-1):
    if a[i] != a[i+1]:
        count += 1
print(count)