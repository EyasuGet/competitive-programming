# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if len(firstList) == 0 or len(secondList) == 0:
            return []


        first = 0
        second = 0
        ans = []
        while first < len(firstList) and second < len(secondList):

            intersection = []

            st1 = firstList[first][0]
            en1 = firstList[first][1]

            st2 = secondList[second][0]
            en2 = secondList[second][1]

            if st1 > st2 and st1 > en2:
                second += 1

            elif st2 > st1 and st2 > en1:
                first += 1
            else:

                intersection.append(max(st1,st2))
                intersection.append(min(en1, en2))

                ans.append(intersection)
                
                if en1 <= en2:
                    first += 1
                else:
                    second += 1

        return ans
            

