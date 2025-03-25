# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstOcc(nums, target):
            ans = -1
            n = len(nums)
            left, right = 0, n -1 
            while left <= right:
                mid = (left+right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid-1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def lastOcc(nums, target):
            ans = -1
            n = len(nums)
            left, right = 0, n -1 
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    ans = mid
                    left = mid+1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans
        
        lower = firstOcc(nums, target)
        upper = lastOcc(nums, target)
        return [lower,upper]