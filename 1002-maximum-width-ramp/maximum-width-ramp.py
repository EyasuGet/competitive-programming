class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ramp = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] <= nums[j]:
        #             ramp = max(ramp,j-i)
            
        # return ramp
        ramp = 0
        st = []
        for i in range(len(nums)):
            if not st or nums[i] < nums[st[-1]]:
                st.append(i)
 
        for j in range(len(nums) - 1, -1, -1):
            while st and nums[st[-1]] <= nums[j]:
                i = st.pop()
                ramp = max(ramp, j - i)

        return ramp