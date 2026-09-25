for _ in range(int(input())):
    
    n , k = map(int, input().split())
    farm = input()
    cost = 0
    
    for i in range(0, n, k):
        
        if "0" not in farm[i: i+k]:
            cost += 1
            
    print(cost)