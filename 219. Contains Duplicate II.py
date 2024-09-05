class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # for l in range(len(nums)):
        #     for r in range(l+1,len(nums)):
        #         if nums[l] == nums[r]:
        #             if (abs(r-l)<=k):
        #                 return True
        # return False

        s = set()
        l = 0
        r = 1
        while r < len(nums) and l <len(nums):
            if (l != r) and (nums[l] == nums[r]):
                if (abs(r-l)<=k):
                    print(l,r)
                    return True
                else:
                    l += 1
            elif nums[r] in s:
                l += 1
            else:
                s.add(nums[r])
                r+=1
        return False
                    
            

        