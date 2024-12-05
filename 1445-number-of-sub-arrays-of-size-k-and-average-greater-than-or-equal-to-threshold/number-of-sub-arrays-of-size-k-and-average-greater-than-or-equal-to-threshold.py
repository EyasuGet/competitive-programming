class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # count = 0
        # l, r = 0, 0
        # while r< len(arr):
        #     if (r-l+1) == k:
        #         if sum(arr[l:r+1]) / k >= threshold:
        #             count += 1
        #             l += 1
        #             r += 1
        #         else:
        #             l += 1
        #             r += 1
        #     else:
        #         r += 1
        # return count

        l = 0
        summ = 0
        count = 0
        for r in range(len(arr)):
            summ += arr[r]
            if (r-l + 1) == k:
                if summ / k >= threshold:
                    count += 1
                summ -= arr[l]
                l += 1
        return count





        