# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict

t = int(input())
prefix = defaultdict(int)
for _ in range(t):
    ranges = list(map(int, input().split()))
    prefix[ranges[0]] += 1
    prefix[ranges[1]+1] -= 1

key = sorted(prefix.keys())
#the running sum will contain the prefix range update array with in the range
ans = defaultdict(int)
running_sum = 0
for i in range(len(key)-1):
    running_sum += prefix[key[i]]

    ans[running_sum] += (key[i+1] - key[i])

#if we have less number of keys in our ans that means we had 0 non overlapping ranges
res = []
for i in range(1, t+1):
    res.append(ans[i])
print(*res)