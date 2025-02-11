# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        minn = abs(min(nums))
        maxx = max(nums)
        count_arr = [0] * (maxx + minn + 1)

        for i in nums:
            count_arr[i + minn] += 1
        
        target = 0
        for idx,val in enumerate(count_arr):

            for i in range(val):
                nums[target] = idx - minn
                target += 1
        return nums