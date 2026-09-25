for i in range(int(input())):
    a, b = map(int, input().split())
    if abs(a - b) % 10 == 0:
        print(abs(a - b)//10)
    else:
        print(abs(a - b)//10 + 1)