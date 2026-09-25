n = int(input())
events = list(map(int, input().split()))
recruits, crimes = 0, 0
for i in events:
    if i == -1 and recruits == 0:
        crimes += 1
    elif i == -1 and recruits > 0:
        recruits -= 1
    elif i != -1:
        recruits += i
print(crimes)