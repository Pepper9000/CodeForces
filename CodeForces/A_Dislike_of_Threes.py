a = []
i = 1
while(len(a) != 1000):
    j = str(i)
    if i % 3 != 0 and j[-1] != "3":
        a.append(i)
    i += 1

for _ in range(int(input())):
    print(a[int(input())-1])