class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # p = []
        # n = []

        # for i in nums:
        #     if i < 0:
        #         n.append(i)
        #     else:
        #         p.append(i)
        # ans  = []
       
        # for i in range(len(p)):
        #     ans.append(p[i])
        #     ans.append(n[i])
        # return ans

        #tc = o(n)
        #sc = o(n)
        l = len(nums)
        ans = [0] * l
        p = 0
        n = 1
        for i in range(l):
            if nums[i] > 0:
                ans[p] = nums[i]
                p += 2
            else:
                ans[n] = nums[i]
                n += 2
        return ans


        
            

            




        

        