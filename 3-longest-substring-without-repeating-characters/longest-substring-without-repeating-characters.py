class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left]) 
                left += 1
            check.add(s[right])
            longest = max(longest, right-left + 1)
        return longest
