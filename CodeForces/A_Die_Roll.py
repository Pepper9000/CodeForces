a, b = map(int, input().split())
if max(a, b) == 1:
    print("1/1")
elif max(a, b) == 2:
    print("5/6")
elif max(a, b) == 3:
    print("2/3")
elif max(a, b) == 4:
    print("1/2")
elif max(a, b) == 5:
    print("1/3")
elif max(a, b) == 6:
    print("1/6")