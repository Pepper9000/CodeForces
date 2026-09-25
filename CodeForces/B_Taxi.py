import math as m 
n = int(input())
a = list(map(int, input().split()))
c1, c2, c3, c4 = a.count(1), a.count(2), a.count(3), a.count(4)
taxi = c4
if c3 >= c1:
    taxi += c3 
    if c2 % 2 == 0:
        taxi += c2//2
    else:
        taxi += m.ceil(c2/2)
elif c3 < c1:
    taxi += c3
    
    if c2 % 2 == 0:
        taxi += c2//2 + m.ceil((c1-c3)/4)
        
    elif c2 % 2 != 0 and (c1-c3) % 4 < 3:
        taxi += c2//2 + (c1-c3)//4 + 1
        
    elif c2 % 2 != 0 and (c1-c3) % 4 > 2:
        taxi += c2//2 + m.ceil((c1-c3)/4) + 1
        
print(taxi)