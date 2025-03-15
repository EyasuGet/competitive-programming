# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        n = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i in s:
            if i != "]":
                st.append(i)
            
            else:
                s = ""
                while st[-1] != "[":
                    s = st.pop() + s
                st.pop()
                num = ""
                while st and st[-1] in n:
                    num = st.pop() + num

                st.append(int(num) * s) 

        return "".join(st)




