# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

def count_good_segments(n, k, a):
    min_dq = deque()
    max_dq = deque()
    ans = 0
    r = 0
    for l in range(n):
        while r < n:
            while min_dq and a[r] < a[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(r)
            
            while max_dq and a[r] > a[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(r)
            
            if a[max_dq[0]] - a[min_dq[0]] > k:
                break
            r += 1

        ans += r - l
        if min_dq and min_dq[0] == l:
            min_dq.popleft()
        if max_dq and max_dq[0] == l:
            max_dq.popleft()
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(count_good_segments(n, k, a))