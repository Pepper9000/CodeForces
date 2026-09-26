for _ in range(int(input())):
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    score = 0
    while n >= k:
        if a[k - 1] > a[n - k]:
            score += a[k - 1]
            a.pop(k - 1)
        else:
            score += a[n - k]
            a.pop(n - k)
        n = n - 1
    print(score)