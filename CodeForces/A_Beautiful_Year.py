a = int(input()) + 1
a = str(a)
while len(set(a)) != 4:
    a = int(a) + 1
    a = str(a)
print(a)