class Solution(object):
    
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #since the heap sort them when pushed we can invert them into a -ve num
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        summ = 0
        while k > 0:
            m = -heapq.heappop(max_heap)
            summ += m
            k -= 1
            heapq.heappush(max_heap, -math.ceil(m/3.0))
        return int(summ)