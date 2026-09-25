import math as m
n=int(input())
b=list(map(int,input().split()))

arr = [True] * ((10 ** 6) + 1)
arr[0] = arr[1] = False
for i in range(2, int(10 ** 3) + 1):
    if arr[i]:
        for xi in range(i * i, (10**6) + 1, i):
            arr[xi] = False 

for i in b:
    if int(m.sqrt(i)) == m.sqrt(i):
        if arr[int(m.sqrt(i))] == True:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")