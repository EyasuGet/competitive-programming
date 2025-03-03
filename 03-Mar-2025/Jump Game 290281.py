# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        tar_idx = n -1
        if n == 1:
            return True

        max_line = 0
        l = 0
        while l < n-1:
            if l > max_line:
                return False
            land = nums[l] + l
            if land >= max_line:
                max_line = land
            l += 1

            if max_line >= tar_idx:
                return True
        
        return False