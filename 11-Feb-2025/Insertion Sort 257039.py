# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    for i in range(1,n):
        
        j = i - 1
        key = arr[i]
        
        while arr[j] > key and j >= 0:
            
            arr[j+1] = arr[j]
            j -= 1
            print(*arr)
            
        arr[j+1] = key
    
    print(*arr)
    