for _ in range(int(input())):
    a = int(input())
    x = list(map(int, input().split()))
    count = 0
    for i in range(a):
        for j in range(i + 1, a):
            if x[j] - x[i] == j - i:
                count += 1
    print(count)