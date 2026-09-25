n = input()
a = set()
for i in n:
    if i.isalpha():
        a.add(i)
print(len(a))