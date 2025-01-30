class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        
        for i in range(n):
            if i % 2 == 0 and n % 2 == 0:
                return i
        return n * 2
