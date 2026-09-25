h = input()
a = []
for i in h:
    if i == "h" and len(a) == 0:
        a.append(i)
    elif i == "e" and len(a) == 1:
        a.append(i)
    elif i == "l" and len(a) == 2:
        a.append(i)
    elif i == "l" and len(a) == 3:
        a.append(i)
    elif i == "o" and len(a) == 4:
        a.append(i)
if a == ['h','e','l','l','o']:
    print("YES")
else:
    print("NO")