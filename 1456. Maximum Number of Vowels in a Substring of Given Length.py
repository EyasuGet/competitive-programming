class Solution(object):
    def maxVowels(self, s, k):
        vowels = ("a","e","i","o","u")
        answer = []
        count = 0
        max_count = float("-inf")
        for i in range(len(s)):
            answer.append(s[i])
            if s[i] in vowels:
                count += 1
            if (i >= k - 1):
                max_count = max(max_count,count)
                if s[i - (k - 1)] in vowels:
                    count -= 1
                answer.pop(0)
        return max_count

                
                