for _ in range(int(input())):
    count = 0
    a = int(input())
    b = True
    while a != 1:
        if a % 6 == 0:
            a = a / 6
            count += 1
        elif a % 3 == 0:
            a = a * 2
            count += 1
        else:
            print(-1)
            b = False
            break
    if b:
        print(count)