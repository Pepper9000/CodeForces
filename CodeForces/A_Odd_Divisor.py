for i in range(int(input())):
    n = str(bin(int(input())))
    count = 0
    for j in n:
        if j == "1":
            count += 1
    if count == 1:
        print("NO")
    else:
        print("YES")    