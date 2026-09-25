n = input()
if (n[1:].isupper() and n[0].islower()) or n.isupper():
    print(n.swapcase())
elif len(n) == 1:
    print(n.swapcase())
else:
    print(n)