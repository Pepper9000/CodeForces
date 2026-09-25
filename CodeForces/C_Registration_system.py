a = {}
for i in range(int(input())):
    n = input()
    if n not in a:
        a[n] = 0
        print("OK")
    else:
        a[n] += 1
        print(f"{n}{a[n]}")