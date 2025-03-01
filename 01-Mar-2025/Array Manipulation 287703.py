# Problem: Array Manipulation - https://www.hackerrank.com/challenges/crush/problem

from itertools import accumulate
def arrayManipulation(n, queries):
    prefix = [0] * (n+1)
    for left , right, k in queries:
        prefix[left-1] += k
        
        prefix[right] -= k
    p = list(accumulate(prefix))
    
    return max(p)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()