for _ in range(int(input())):
    
    n = int(input())
    a = list(map(int, input().split()))
    x = set(a)
    x = sorted(list(x))
    y = []
    
    for i in x:
        y.append(x.count(i)) 
    
    