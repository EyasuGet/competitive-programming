# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        count_arr = [0] * (max(nums) + 1)

        for i in nums:
            count_arr[i] += 1

        targ = 0
        for idx, val in enumerate(count_arr):

            for i in range(val):
                nums[targ] = idx
                targ += 1

        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                
                ans.append(i)
        return ans     