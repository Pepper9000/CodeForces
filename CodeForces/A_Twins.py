int(input())
sloth = list(map(int, input().split()))
sloth = sorted(sloth, reverse = True)
sloth_amt = sum(sloth)
greed = 0
i = 0
while(greed <= sloth_amt):
    greed += sloth[i]
    sloth_amt -= sloth[i]
    i += 1
print(i)