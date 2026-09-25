n, m = map(int, input().split())
count = 0
for i in range(1, n+1):
    if i % 2 != 0:
        print("#"*m)
    elif i % 2 == 0 and count % 2 == 0:
        print("."*(m-1)+"#")
        count += 1
    elif i % 2 == 0 and count % 2 != 0:
        print("#"+"."*(m-1))
        count += 1