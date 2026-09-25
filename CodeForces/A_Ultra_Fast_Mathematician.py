a = input()
b = input()
for i in range(len(a)):
    print("0",end="") if a[i] == b[i] else print("1",end="")