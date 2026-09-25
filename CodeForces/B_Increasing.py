for _ in range(int(input())):
    b = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == b:
        print("YES")
    else:
        print("NO")