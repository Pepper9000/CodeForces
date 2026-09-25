for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    easy = a.count(0)

    if easy < 2:
        print(-1)
    elif a[0] == 0 and a[-1] == 0:
        print(0)
    elif a[0] == 1 and a[-1] == 1:
        print(2)
    else:
        print(1)