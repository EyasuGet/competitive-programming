# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())
for _ in range(t):
    nums = sorted(map(int, input().split()))
    if nums[-1] == nums[0] + nums[1]:
        print("YES")
    else:
        print("NO")
    