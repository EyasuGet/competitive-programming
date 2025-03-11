# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    nums = input()

    zero = []
    one = []
    ans = []
    sub = 0

    for i in nums:
        if i == "0":

            if one:
                current_sub = one.pop()
                ans.append(current_sub)
                zero.append(current_sub)
            else:
                sub += 1
                current_sub = sub
                zero.append(current_sub)
                ans.append(current_sub)
        else:
            if zero :
                current_sub = zero.pop()
                ans.append(current_sub)
                one.append(current_sub)
            else:
                sub += 1
                current_sub = sub
                one.append(current_sub)
                ans.append(current_sub)
    print(sub)
    print(*ans)