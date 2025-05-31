# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

def max_prefix_sum(arr):
    max_sum = 0
    current = 0
    for x in arr:
        current += x
        max_sum = max(max_sum, current)
    return max_sum

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    ans = max_prefix_sum(r) + max_prefix_sum(b)
    print(ans)