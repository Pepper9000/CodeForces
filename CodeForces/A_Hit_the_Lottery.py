n = int(input())
count = 0
a = [100, 20, 10, 5, 1]
for i in a:
    if n >= i:
        count += n // i
        n = n % i 
print(count)