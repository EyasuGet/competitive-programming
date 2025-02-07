# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())

from collections import defaultdict
for _ in range(t):
    mat = []
    n , m = map(int, input().split())
    for i in range(n):
        row = list(map(int, input().split()))
        mat.append(row)


    main_sum = defaultdict(int)
    cross_sum = defaultdict(int)


    for i in range(n):
        for j in range(m):
            main_sum[i-j] += mat[i][j]
            cross_sum[i+j] += mat[i][j]
    
    res = 0
    for i in range(n):

        for j in range(m):
            curr = main_sum[i-j] + cross_sum[i+j] - mat[i][j]
            res = max(curr,res)
    print(res)