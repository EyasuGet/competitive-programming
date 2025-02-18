# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

ans = float("inf")
for i in range(97,123):
    char = chr(i)
    left = 0
    right = n -1
    curr = 0 
    while left < right:
        if str1[left] == str1[right]:
            left += 1
            right -= 1
        else:
            if str1[left] == char:
                curr += 1
                left += 1
            elif str1[right] == char:
                curr += 1
                right += 1
            else:
                break
    else:
        ans = min(ans, curr)ans = float("inf")
for i in range(97,123):
    char = chr(i)
    left = 0
    right = n -1
    curr = 0 
    while left < right:
        if str1[left] == str1[right]:
            left += 1
            right -= 1
        else:
            if str1[left] == char:
                curr += 1
                left += 1
            elif str1[right] == char:
                curr += 1
                right += 1
            else:
                break
    else:
        ans = min(ans, curr)