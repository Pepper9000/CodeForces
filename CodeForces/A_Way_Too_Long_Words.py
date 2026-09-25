a = int(input(""))

for n in range(a):
    i = input()

    if len(i) > 10:
        print(f"{i[0]}{len(i)-2}{i[-1]}")
    else:
        print(i)