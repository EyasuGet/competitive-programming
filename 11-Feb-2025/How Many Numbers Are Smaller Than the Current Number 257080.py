# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        for i in nums:
            c = 0
            for num,val in freq.items():
                if num < i:
                    c += val
            ans.append(c)
        return ans
