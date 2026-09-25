for _ in range(int (input())):
    a, b, c = map(int, input().split())
    if a < b and b > c:
        print("PEAK")
    elif a < b and b < c:
        print("STAIR")
    else:
        print("NONE")