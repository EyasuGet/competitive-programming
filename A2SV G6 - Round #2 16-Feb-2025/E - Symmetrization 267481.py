# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

from collections import defaultdict


t  = int(input())

# i , j

# n- j - 1 , i

# n - i - 1, n - j - 1

# n - j -1 , i






for _  in range(t):
    n = int(input())

    mat = []
    for i in range(n):
        row = list(map(int, input()))
        mat.append(row)

    #rotate 90deg
    mat1 = [list(row) for row in zip(*mat[::-1])]

    #rotate mat1 to get 180deg of mat
    mat2 = [list(row) for row in zip(*mat1[::-1])]

    #rotate mat2 to get 270deg of mat
    mat3 = [list(row) for row in zip(*mat2[::-1])]


    ans = 0
    for i in range(n//2):
        for j in range(i, n-i-1):
            count_zero_one = defaultdict(int)
            count_zero_one[mat[i][j]] += 1
            count_zero_one[mat1[i][j]] += 1
            count_zero_one[mat2[i][j]] += 1
            count_zero_one[mat3[i][j]] += 1
            
            
            if count_zero_one[0] > count_zero_one[1]:
                ans += count_zero_one[1]
            else:
                ans += count_zero_one[0]

    print(ans)
