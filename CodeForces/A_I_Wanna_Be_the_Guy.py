n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
p.pop(0)
q.pop(0)
if 0 in set(p+q):
    if len(set(p+q)) == n+1:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
else:
    if len(set(p+q)) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")