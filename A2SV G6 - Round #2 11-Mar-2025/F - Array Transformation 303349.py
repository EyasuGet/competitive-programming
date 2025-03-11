# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from typing import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    freq = Counter(nums)
    
    count_freq = list(freq.values())
    count_freq.sort()

    removed = float("inf")
    for i in range(len(count_freq)):
        removed = min((n- (len(count_freq) - i) * count_freq[i]), removed)
    print(removed)
    