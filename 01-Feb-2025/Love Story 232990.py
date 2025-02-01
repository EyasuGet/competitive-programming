# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
for _ in range(t):
    str1 = input()
    s = "codeforces"
    
    p = 0
    count = 0
    while p < 10:
        if str1[p] != s[p]:
            count += 1
        p += 1
    print(count)
    