# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    count = i = 0
    while i< n-1:
        if nums[i+1] < nums[i]:
            i += 2
            count +=1 
        else:
            i +=1 

    print(count)