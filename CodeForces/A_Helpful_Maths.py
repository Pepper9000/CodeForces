a = list(map(int, input().split("+")))
a.sort()
for i in range(len(a)-1):
    print(f"{a[i]}+",end="")
print(a[-1])