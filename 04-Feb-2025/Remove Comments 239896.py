# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        
        s = "~".join(source)

        ans = ""
        st = 0
        while st < len(s):

            if st < len(s) -1 and (s[st] == "/" and s[st+1] == "*"):
                st += 2

                while st < len(s)- 1 and s[st] + s[st + 1] != "*/":
                    st += 1
                else:
                    st += 2

            elif st < len(s) -1 and (s[st] == "/" and s[st+1] == "/"):
                while st < len(s) and s[st] != "~":  
                    st += 1
            else:
                ans += s[st]
                st += 1 
    
        res = ans.split("~")
        ans = []
        for i in res:
            if len(i) != 0:
                ans.append(i)
        
        return ans

                    
            
                        