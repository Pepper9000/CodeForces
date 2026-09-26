for _ in range(int(input())):
    
    n, k = map(int, input().split())
    power = n - k  + 1
    money = (2 ** power) + 2*(k -1)
    print(money)