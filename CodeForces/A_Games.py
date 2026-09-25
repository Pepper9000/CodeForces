n = int(input())
home, away, ans = [], [], 0
for i in range(n):
    x = list(map(int, input().split()))
    home.append(x[0])
    away.append(x[1])
for i in range(n):
    if home[i] == away[i]:
        ans += away.count(home[i]) - 1
    else:
        ans += away.count(home[i])
print(ans)