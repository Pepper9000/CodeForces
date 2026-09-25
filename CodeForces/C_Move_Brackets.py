for _ in range(int(input())):
    a = int(input())
    b = input()
    open = 0 
    while "()" in b:
        b = b.replace("()", "")
    print(len(b)//2)