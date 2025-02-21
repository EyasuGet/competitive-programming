# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())

def validate(l, r,letter, str1):

    ans = 1
    while l < r:
        if str1[l] == str1[r]:
            l += 1
            r -= 1

        else:
            if str1[l] == letter:
                l += 1
                ans += 1
            elif str1[r] == letter:
                r -= 1
                ans += 1
            else:
                return -2
    return ans


for _ in range(t):
    n = int(input())
    str1 = input()
    l = 0
    r = n - 1

    while l < r:

        if str1[l] == str1[r]:
            l += 1
            r -= 1
        else:
            validate_right = validate(l+1, r, str1[l], str1)
            validate_left = validate(l, r-1,str1[r], str1)

            if validate_left < 0 and validate_right >= 0:
                print(validate_right)
                break

            elif validate_right < 0 and validate_left >= 0:
                print(validate_left)
                break

            elif validate_left >= 0 and validate_right>= 0 :
                ans = min(validate_right, validate_left)
                print(ans)
                break

            else:
                print(-1)
                break
    if l >= r:
        print(0)