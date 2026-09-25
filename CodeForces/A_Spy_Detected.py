for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = sorted(a)
    if b[0] == b[1]:
        print(a.index(max(a))+1)
    else:
        print(a.index(min(a))+1)