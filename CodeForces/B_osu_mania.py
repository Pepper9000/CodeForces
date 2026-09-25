for _ in range(int(input())):
    n = int(input())
    x = []
    for i in range(n):
        x.insert(0, input().index("#")+1)
    print(*x)