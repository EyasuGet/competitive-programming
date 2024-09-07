import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # n = len(nums)
        # s = sorted(nums)
        # return s[n-k]
        #tc = o(1)
        #sc = o(n)

        # we can use minheap in the heapq library it will build them
        # internally as a kinda tree in o(n) time
        # since it is not a maxheap we have to mulyiply
        # the values by -ve

        # it will build the heap in o(n) time and in place that is o(1)
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums) #log(n) times to pop
        
        return -heapq.heappop(nums)

        #tc =  0(N + klog(n))
        #sc = 0(1)
        