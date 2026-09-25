n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print("0") if a % b == 0 else print(b - (a % b))