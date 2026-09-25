a = int(input())
b = [4, 7, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]
lucky = False
for i in b:
    if a % i == 0:
        lucky = True
if lucky:
    print("YES")
else:
    print("NO")