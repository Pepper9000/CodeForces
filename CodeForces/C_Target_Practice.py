for _ in range(int(input())):
    value = []
    point = 0
    for i in range(10):
        value.append(input())
    for i in range(10):
        for j in range(10):
            if value[i][j] == "X":
                if i == 0 or i == 9 or j == 0 or j == 9:
                    point += 1
                elif i == 1 or i == 8 or j == 1 or j == 8:
                    point += 2
                elif i == 2 or i == 7 or j == 2 or j == 7:
                    point += 3
                elif i == 3 or i == 6 or j == 3 or j == 6:
                    point += 4
                elif i == 4 or i == 5 or j == 4 or j == 5:
                    point += 5
    print(point)