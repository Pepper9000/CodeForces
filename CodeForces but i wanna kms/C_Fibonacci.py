n = int(input()) - 1
a = [0, 1]

while n != 0:
    
    b = a[1]
    a[1] = sum(a)
    a[0] = b
    n -= 1

print(a[1] % (10 ** 9 + 7))