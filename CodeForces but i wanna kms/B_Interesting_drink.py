n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())

for i in range(q):
    count = 0
    m = int(input())
    if x[-1] <= m:
        print(len(x))
    elif x[0] > m:
        print(0)
    elif m in x:
        print(x.index(m) + x.count(m))
    else:
        for j in x:
            if  j <= m:
                count += 1
            else:
                break
        print(count)