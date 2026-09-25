a = input()
b = []
for i in a:
    b.append(i)
    if i == "." and len(b) == 1:
        print(0, end = "")
        b = []
    if len(b) == 2:
        if "-" in b and "." not in b:
            print(2, end = "")
            b = []
        elif "-" in b and "." in b:
            print(1, end = "")
            b = []