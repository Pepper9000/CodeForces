cost, coin = map(int, input().split())
count = 1
while True:
    if (cost * count) % 10 == 0 or (cost * count - coin) % 10 == 0:
        break
    else:
        count += 1
print(count)