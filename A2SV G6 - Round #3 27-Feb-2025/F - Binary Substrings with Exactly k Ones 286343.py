# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import Counter

n = int(input())
binary = input()

dic = Counter({0:1})
ans = 0
tot = 0
for r in range(len(binary)):
    tot += int(binary[r])
    ans += dic[tot - n]
    dic[tot] += 1
    
print(ans) 