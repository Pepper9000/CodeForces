house, tasks = map(int, input().split())
a = list(map(int, input().split()))
time = a[0]
for i in range(len(a)-1):
    if a[i+1] > a[i]:
        time += a[i+1] - a[i]
    elif a[i+1] == a[i]:
        continue
    else:
        time += house - a[i] + a[i+1]
print(time - 1)