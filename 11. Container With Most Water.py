class Solution(object):
    def maxArea(self, height):
        # max_water = 0
        # for i in range(0,len(height)-1):
        #     for j in range(i+1,len(height)):
        #         length = min(height[i],height[j])
        #         curr_water = length * (j - i)
        #         if curr_water > max_water:
        #             max_water = curr_water
        # return max_water

        i = 0
        j = len(height) - 1
        max_water = 0
        while i < j:
            length = min(height[i], height[j])
            curr_water = length * (j - i)
            if curr_water > max_water:
                max_water = curr_water
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_water  


        