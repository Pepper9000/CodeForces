for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    count = 0
    for i in x:
        if i % 2 != 0:
            count += 1
    if len(x) == 1 or count % 2 != 0:
        print("NO")
    else:
        print("YES") 