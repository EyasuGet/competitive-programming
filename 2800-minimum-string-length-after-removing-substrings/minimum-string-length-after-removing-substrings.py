class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        for i in s:
            st.append(i)
            if len(st) >= 2:
                c = st[-2] + st[-1]
                if c == "AB" or c == "CD":
                    st.pop()
                    st.pop()
        return len(st)