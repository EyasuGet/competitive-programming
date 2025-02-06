# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        evensum = 0

        for i in nums:
            if i % 2 == 0:
                evensum += i
        
        for val,idx in queries:
            if nums[idx] % 2 == 0 and val % 2 == 0:
                evensum += val
                nums[idx] += val
                ans.append(evensum)

            elif nums[idx] % 2 == 1 and val % 2 == 1:
                evensum += (nums[idx] + val)
                nums[idx] += val
                ans.append(evensum)

            elif nums[idx] % 2 == 1 and val % 2 == 0:
                nums[idx] += val
                ans.append(evensum)
            else:
                evensum -= nums[idx]
                nums[idx] += val
                ans.append(evensum)

        return ans



        