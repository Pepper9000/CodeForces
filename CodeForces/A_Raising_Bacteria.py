bacteria = int(input())
count = 0
while(bacteria != 0):
    if bacteria % 2 != 0:
        count += 1
        bacteria -= 1
    else:
        bacteria = bacteria / 2
print(count)