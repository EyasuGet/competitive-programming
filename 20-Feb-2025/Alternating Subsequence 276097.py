# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))


    left = right= 0 
    ans = 0
    while right < n:
        maxx = nums[right]

        while right < n-1 and ((nums[right] > 0 and nums[right+1] > 0) or (nums[right] < 0 and nums[right+1] < 0) ):
            right += 1   
            maxx = max(maxx, nums[right])

        right += 1
        ans += maxx
    print(ans)