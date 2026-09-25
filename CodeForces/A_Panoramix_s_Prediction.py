n, m = map(int, input().split())
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if m in p:
    if p.index(n) == p.index(m) -1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")