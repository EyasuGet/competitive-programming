# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    swap = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap += 1
    print("Array is sorted in " + str(swap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))