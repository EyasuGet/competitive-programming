# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

from math import ceil, floor

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[floor((n - 1) / 2)])