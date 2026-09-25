for i in range(int(input())):
    a = input()
    b = []
    for j in a:
        b.append(int(j))
    if sum(b[:3]) == sum(b[3:]):
        print("YES")
    else:
        print("NO")