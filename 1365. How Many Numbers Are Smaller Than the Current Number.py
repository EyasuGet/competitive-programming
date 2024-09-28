class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: List[int]
        # """
        # n = len(nums)
        # ans = [0] * n

        # #brute force
        # for i in range(n):
        #     c = 0
        #     for j in nums:
        #         if j < nums[i]:
        #             c += 1
        #         ans[i] = c
        # return ans

        #sort
        # ans = []
        # num = sorted(nums)
        # for i in nums:
        #     c = 0
        #     for j in range(len(num)):
        #         if num[j] == i:
        #             ans.append(c)
        #             break
        #         else:
        #             c += 1
        # return ans

        #using hashmap
        ans= []
        temp = sorted(nums)
        hash_map = {}
        for i in range(len(nums)):
            if temp[i] not in hash_map:
                hash_map[temp[i]] = i
        for i in range(len(nums)):
            ans.append(hash_map[nums[i]])
        return ans

        