for _ in range(int(input())):
    a, b = map(int, input().split())
    gas = list(map(int, input().split()))
    dist = gas[0]
    for i in range(a - 1):
        dist = max(gas[i+1] - gas[i], dist)
    print(max(dist, (2 * (b - gas[-1])) ))