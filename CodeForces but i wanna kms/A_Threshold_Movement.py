for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    if n % 2 != 0:
        print("NO")
    else:
        b = []
        a=10**8
        for i in range(0, n, 2):
            a=min(a, abs(x[i] - x[i+1]))