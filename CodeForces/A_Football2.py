teams = []
goals = []
for _ in range(int(input())):
    a = input()
    if a in teams:
        goals[teams.index(a)] += 1
    else:
        teams.append(a)
        goals.append(1)
x = goals.index(max(goals))
print(teams[x]) 