a = list(map(int, input().split()))
s = input()
calories = 0
for i in s:
    if i == "1":
        calories += a[0]
    elif i == "2":
        calories += a[1]
    elif i == "3":
        calories += a[2]
    elif i == "4":
        calories += a[3]
print(calories)