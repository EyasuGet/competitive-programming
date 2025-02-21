# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n , k, q = map(int,input().split())
recipes = []
for _ in range(n):
    recipes.append(list(map(int, input().split())))

question = []
for _ in range(q):
    question.append(list(map(int, input().split())))

# marking the ranges
prefix = [0] * 200002
for rec in recipes:
    start, end = rec
    prefix[start] += 1
    prefix[end + 1] -= 1

#forming the prefix sum
for i in range(1,len(prefix)):
    prefix[i] += prefix[i-1]

#if the the count is greater than k we will add the previous count and itself(considering it as one)
# 1 2 2 2 1 1 2 1 1 0 .. # print(prefix[91:101]) the second prefix
# 0 1 2 3 3 3 4 4 4 4 .. the third prefix
for i in range(1,len(prefix)):
    prefix[i] = prefix[i-1] + (1 if prefix[i] >= k else 0)

for q in question:
    start, end = q
    count = prefix[end] - prefix[start-1]
    print(count)