# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter, defaultdict
t = int(input())

def check(str1):
    right = Counter(str1)
    left = defaultdict(int)

    ans = 0
    for i in str1:
        left[i] += 1
        right[i] -= 1

        if right[i] == 0:
            del right[i]

        ans = max(ans, len(left) + len(right))
            
    return ans
for _ in range(t):
    n = int(input())
    str1 = input()

    print(check(str1))