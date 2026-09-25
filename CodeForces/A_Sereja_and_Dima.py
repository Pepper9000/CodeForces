n = int(input())
x = list(map(int, input().split()))
seerja, dima = 0, 0
for i in range(n//2):
    if x[0] >= x[-1]:
        seerja += x.pop(0)
    else:
        seerja += x.pop(-1)
    if x[0] >= x[-1]:
        dima += x.pop(0)
    else:
        dima += x.pop(-1)
if len(x) == 1:
    seerja += x[0]
print(seerja, dima)