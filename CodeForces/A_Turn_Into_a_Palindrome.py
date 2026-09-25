for _ in range(int(input())):
    
    n, c = input().split()
    n = int(n)
    s = input()
    count = 0
    
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i] == c or s[n - i - 1] == c:
                count += 1
            else:
                count += 2
    
    print(count)