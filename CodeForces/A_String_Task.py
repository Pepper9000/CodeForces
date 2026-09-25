a = list(input().lower())
for i in range(len(a)):
    if a[i] not in ["a","e","i","o","u","y"]:
        print(f".{a[i]}", end="")