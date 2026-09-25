input()
t = list(map(int, input().split()))
print(min(t.count(1), t.count(2), t.count(3)))
for i in range(min(t.count(1), t.count(2), t.count(3))):
    print(t.index(1) + 1, t.index(2) + 1, t.index(3) + 1)
    t[t.index(1)] = "x"
    t[t.index(2)] = "x"
    t[t.index(3)] = "x"