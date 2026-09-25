for _ in range(int(input())):
    int(input())
    s = list(input())
    balloons = 2 * len(set(s))
    a = set(s)
    for i in a:
        balloons += s.count(i) - 1
    print(balloons)