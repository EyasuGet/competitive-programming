# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        main = Counter(s)
        count = 0
        check = set()
        ans = []

        for i in range(len(s)):
            
            main[s[i]] -= 1

            #it helps us check if we found all the elements
            check.add(s[i])
            count += 1

            #if we found all the elements in s we remove it from the set
            if main[s[i]] == 0:
                check.remove(s[i])

            #if there is nothing in the set we found the distinct substring
            #we append the length of the string which is count
            if not check:
                ans.append(count)
                count = 0
        return ans