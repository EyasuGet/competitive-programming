# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

n = int(input())
parents = [0] + [int(input()) for _ in range(n - 1)]
 
children = [[] for _ in range(n + 1)]
for child in range(2, n + 1):
    parent = parents[child - 1]
    children[parent].append(child)
 
is_spruce = True
for i in range(1, n + 1):
    if children[i]:
        leaf_children = 0
        for ch in children[i]:
            if not children[ch]:
                leaf_children += 1
        if leaf_children < 3:
            is_spruce = False
            break
 
print("Yes" if is_spruce else "No")