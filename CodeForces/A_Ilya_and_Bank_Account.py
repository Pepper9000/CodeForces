a = input()
print(max(int(a[:-1]), int(a[:-2]+a[-1])) if int(a) < 0 else a)