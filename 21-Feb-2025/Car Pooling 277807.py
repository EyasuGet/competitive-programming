# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        count = [0] * 1001

        for trip in trips:
            passanger, start, end = trip

            count[start] += passanger
            count[end ] -= passanger
        for i in range(1, len(count)):
            count[i] += count[i-1]
        if max(count) > capacity:
            return False
        else:
            return True
