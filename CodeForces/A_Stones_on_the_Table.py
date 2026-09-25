a = int(input())
b = list(map(str, input()))
count = 0
for i in range(len(b) - 1):
    if b[i] == b[i + 1]:
        count += 1
print(count)