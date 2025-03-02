# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from itertools import accumulate

t = int(input())
nums = list(map(int, input().split()))
prefix1 = [0] + list(accumulate(nums))
# print(prefix1)

num2 = sorted(nums)
prefix2 = [0] + list(accumulate(num2))
# print(prefix2)

q = int(input())
queries = []
for _ in range(q):
    typp , l , r = map(int, input().split())
    if typp == 1:
        print(prefix1[r] - prefix1[l-1])
    else:
        print(prefix2[r] - prefix2[l-1])
