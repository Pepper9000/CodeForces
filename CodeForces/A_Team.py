count = 0

for i in range(int(input())):
    a = map(int, input().split())
    b = sum(a)
    
    if b > 1:
        count += 1

print(count)