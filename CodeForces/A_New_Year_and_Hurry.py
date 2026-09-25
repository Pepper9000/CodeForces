n, k = map(int, input().split())
time_for_problem = 240 - k
count = 0
for i in range(1, n+1):
    if time_for_problem - (i*5) >= 0:
        time_for_problem -= (i*5)
        count += 1
    else:
        break
print(count)