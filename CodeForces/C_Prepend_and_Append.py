for _ in  range(int(input())):
    n = int(input())
    b = input()
    b = list(b)
    for i in range(n//2):
        if b[0] == b[-1]:
            break
        else:
            b.pop(0)
            b.pop(-1)
    print(len(b))