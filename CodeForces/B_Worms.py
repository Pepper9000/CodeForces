n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

prefix_sum_a = [a[0]]

for i in a[1:]:
    prefix_sum_a.append(prefix_sum_a[-1] + i)

def binary_search(arr, target, left, right):
    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left + 1

for i in q:
    print(binary_search(prefix_sum_a, i, 0, n - 1))