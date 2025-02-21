# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)

        closest = float("inf")
        right = len(nums)-1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:

                summ = nums[i] + nums[left] + nums[right]
                
                if abs(summ - target) < abs(closest - target):
                    closest = summ

                if summ == target:
                    return target
                
                elif summ < target:
                    left += 1
                else:
                    right -= 1

        return closest

       