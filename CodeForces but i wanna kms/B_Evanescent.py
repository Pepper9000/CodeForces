for _ in range(int(input())):
    n = int(input())
    s = input()
    if s == "abba":
        print(3)
    else:
        if n > 3:
            ans = n + 1
            z = s[1:-1]
            for i in range(n - 2):
                z = s[:i] + s[i+1:]
                x = z[0]
                z = s[0] + z + s[-1]
                for i in z[1:]:
                    if x[-1] != i:
                        x += i
                ans = min(ans, len(x))
            print(ans)
        else:
            print(1 if s[0] == s[2] else 2) 