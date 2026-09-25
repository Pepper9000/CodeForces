for _ in range(int(input())):
    n = int(input())
    if n % 4 == 0:
        print("YES")
        even = []
        odd = []
        for i in range(2, n + 1, 2):
            even.append(i)
            odd.append(i - 1)
        odd[-1] += sum(even) - sum(odd)
        print(*even, *odd)
    else:
        print("NO")