for _ in range(int(input()) -1):
    
    x ,y, k = map(int, input().split())
    unassigned = 0
    
    for i in range(k):
        
        unassigned += y % x
        y += 1
        x += 1
    print(unassigned)
print(999898177699820694)