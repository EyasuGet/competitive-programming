# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        l = 0
        r = n - 1
        water = 0
        while l < r:
            width = r - l
            ht = min(height[l],height[r])
            water = max(water , width * ht)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return water