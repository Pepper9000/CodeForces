a = input()
low = 0
up = 0
for i in range(len(a)):
    if a[i].isupper():
        up += 1
    else:
        low += 1
if up > low:
    print(a.upper())
elif up <= low:
    print(a.lower())