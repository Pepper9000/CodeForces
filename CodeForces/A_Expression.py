a = int(input())
b = int(input())
c = int(input())
n = [a*b*c, a*(b+c), a+b*c,(a+b)*c, a+b+c]
print(max(n))