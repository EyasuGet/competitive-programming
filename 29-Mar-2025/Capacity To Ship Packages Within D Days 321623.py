# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def validate(capacity):
            weight = 0
            day = 1
            
            for i in weights:

                if weight + i > capacity:
                    day += 1
                    weight = 0
                weight += i
            return day <= days

        l = max(weights)
        r = sum(weights)
        ans  = r
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans