for _ in range(int(input())):
    a = input()
    if "0" in a:
        a = a.replace("0", "", 1)
    if "1" in a:
        a = a.replace("1", "", 1)
    print(a)