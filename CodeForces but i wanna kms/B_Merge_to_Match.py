for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split()))) 
    if a == b:
        print("YES")

        