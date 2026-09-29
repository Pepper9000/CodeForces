for _ in range(int(input())):
    
    p = input()
    num = int(p[1])
    rnsk = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(1, 9):
        
        if i != num:
            print(p[0], end = "")
            print(i)
    for i in rnsk:
        
        if i != p[0]:
            print(i + p[1])