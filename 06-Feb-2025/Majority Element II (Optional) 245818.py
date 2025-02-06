# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = int(len(nums) / 3)

        ans = []
        freq = Counter(nums)

        for key,value in freq.items():
            if value > count:
                ans.append(key)
        return ans