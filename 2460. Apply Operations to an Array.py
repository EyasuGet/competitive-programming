class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = 0
        r = 1
        while r < n:
            if nums[l] == nums[r]:
                nums[l] *= 2
                nums[r] = 0
            l += 1
            r += 1
            
        #moving the zeroes
        n = []
        for i in nums:
            if i != 0:
                n.append(i)
        no_of_zeros = len(nums) - len(n)
        return n + [0] * no_of_zeros
        