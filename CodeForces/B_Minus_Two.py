for _ in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    codd, ceven, c4 = 0, 0, 0
    
    for i in a:
        
        if i % 2 == 1:
            codd += 1
        elif i % 4 == 0:
            c4 += 1
        else:
            ceven += 1
    
    print(max(codd, ceven, c4))