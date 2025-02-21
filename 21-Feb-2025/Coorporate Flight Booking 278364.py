# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        count = [0] * (n)
        for first, last, seats in bookings:
            count[first - 1] += seats
            if last-1 < n - 1:
                count[last] -= seats
    
        
        return list(accumulate(count))
        