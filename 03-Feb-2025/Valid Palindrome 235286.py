# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = ""
        for i in s:
            if 64 < ord(i) < 123 or ord("0") <= ord(i) <= ord("9"):  #checking if its in range A-Z and a - z
                if 91 <= ord(i) <= 96: #excluding some characters between Z and a
                    continue
                else:
                    str1 += i.lower()
        
        l = 0
        r = len(str1) -1
       
        while l < r:
            if str1[l] != str1[r]:
                return False
            l += 1
            r -= 1
        return True

        