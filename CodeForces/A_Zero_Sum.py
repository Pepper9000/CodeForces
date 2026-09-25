for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    if a % 2 != 0:
        print("NO")
    else:
        if abs(sum(b)) % 4 == 0:
            print("YES")
        else:
            print("NO")