class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        events = sorted([(arr, leave, i) for i, (arr, leave) in enumerate(times)])
        available_chairs = []
        heapq.heapify(available_chairs)
        
        leaving_heap = []
        next_available_chair = 0
        for arr, leave, friend in events:
            while leaving_heap and leaving_heap[0][0] <= arr:
                _, chair_to_free = heapq.heappop(leaving_heap)
                heapq.heappush(available_chairs, chair_to_free)

            if available_chairs:
                chair = heapq.heappop(available_chairs)
            else:
                chair = next_available_chair
                next_available_chair += 1
            
            if friend == targetFriend:
                return chair
            
            heapq.heappush(leaving_heap, (leave, chair))
            