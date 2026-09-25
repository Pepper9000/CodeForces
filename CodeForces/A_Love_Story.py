for _ in range(int(input())):
    ans = "codeforces"
    new = input()
    count = 0
    for i in range(10):
        if ans[i] != new[i]:
            count += 1
    print(count)