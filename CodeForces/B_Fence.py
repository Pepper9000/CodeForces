n, k = map(int, input().split())
fence = list(map(int, input().split()))

current = sum(fence[:k])
minimum = current
index = 0

for i in range(1, n - k + 1):
    current = current - fence[i - 1] + fence[i + k - 1]

    if current < minimum:
        minimum = current
        index = i

print(index + 1)