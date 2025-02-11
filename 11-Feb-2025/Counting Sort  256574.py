# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    
    count_arr = [0] * 100
    
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    
    return count_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()