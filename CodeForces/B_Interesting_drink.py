n = int(input())
x = sorted(list(map(int, input().split())))
q = int(input())

def binary_search(arr, target, left, right):
    
    if left > right:
        return left

    mid = left + (right - left) // 2

    if arr[mid] <= target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

for i in range(q):
    m = int(input())
    print(binary_search(x, m, 0, len(x) - 1))