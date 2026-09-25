summ = int(input())
a = []
if summ == 1:
    print(1)
else:
    while summ >= sum(a):
        a.append(((len(a) + 1) * ((len(a) + 1) + 1)) // 2)
    print(len(a) - 1)