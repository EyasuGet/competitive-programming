# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l
        p = 0
        n = 1
        for i in range(l):
            if nums[i] > 0:
                ans[p] = nums[i]
                p += 2
            else:
                ans[n] = nums[i]
                n += 2
        return ans

