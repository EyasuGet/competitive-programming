# Problem: Books - https://codeforces.com/contest/279/problem/B

n ,time = map(int, input().split())
book = list(map(int, input().split()))

l = 0
summ = 0
maxx = 0
for r in range(n):
    summ += book[r]
    while summ > time:
        summ -= book[l]
        l += 1
    maxx = max(maxx, r + 1 - l)
print(maxx)