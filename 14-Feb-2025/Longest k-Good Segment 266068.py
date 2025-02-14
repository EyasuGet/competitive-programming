# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict


n, m = map(int, input().split())

nums = list(map(int, input().split()))

check = defaultdict(int)
l = 0
start = end = 0

maxx = 0
for r in range(len(nums)):
    check[nums[r]] += 1

    while len(check) > m:
        check[nums[l]] -= 1

        if check[nums[l]] == 0:
            del check[nums[l]]
        l += 1
    dis = r - l +1
    if dis > maxx:
        start = l+1
        end = r + 1
        maxx = max(maxx, r - l + 1)

print(start, end)