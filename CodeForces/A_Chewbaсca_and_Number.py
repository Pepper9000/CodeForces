a = input()
b = ''
for i in range(len(a)):
    if int(a[i]) >= 5:
        b += str(9 - int(a[i]))
    else:
        b += a[i]
if b[0] == "0":
    print("9" + b[1:])
else:
    print(b)