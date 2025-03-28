# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n , m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

n1 = len(arr1)
n2 =len(arr2)
l1 = l2 = 0
ans = []

while l1 < n1 and l2 < n2:
    if l1== n1 or arr1[l1] < arr2[l2]:
        ans.append(arr1[l1])
        l1 += 1
    else:
        ans.append(arr2[l2])
        l2 += 1
while l2 < n2:
    ans.append(arr2[l2])
    l2 += 1
while l1 < n1:
    ans.append(arr1[l1])
    l1+=1
print(*ans)


        