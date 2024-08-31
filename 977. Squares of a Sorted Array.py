class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort() #takes nlog(n) time
        return nums

        #to improve the TC 0(n)
        # l = 0
        # r = len(nums) -1
        # answer = []
        # while l <= r:
        #     if (abs(nums[l]) > abs(nums[r])):
        #         answer.append(nums[l] ** 2)
        #         l += 1
        #     else:
        #         answer.append(nums[r] ** 2)
        #         r -= 1
        # answer.reverse()
        # return answer