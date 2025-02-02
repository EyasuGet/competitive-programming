# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array=[]
        for i in range(1,n+1):
            if i % 3==0 and i % 5==0:
                array.append("FizzBuzz")
            elif i%5 == 0:
                array.append("Buzz")
            elif i % 3 == 0:
                array.append("Fizz")
            else:
                array.append(str(i))
        return array