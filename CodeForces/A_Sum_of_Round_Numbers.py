n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in a:
    x = str(i)
    print(len(x) - x.count("0"))
    count = 1
    for j in x:
        if j != "0":
            print(int(j)*10**(len(x)-count), end = " ")
        count += 1
    print()