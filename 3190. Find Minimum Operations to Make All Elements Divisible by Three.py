class Solution(object):
    def minimumOperations(self, nums):
        count=0
        for i in nums:
            if i % 3 == 0:
                continue
            elif (i % 3 == 1):
                count += 1
            elif ((i % 3)+1) % 3 == 0:
                count += 1
            else:
                continue
        return count

        # for i in nums:
        #     if i % 3 != 0:
        #         x += 1
        # return x