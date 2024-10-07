class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        for i in s:
            st.append(i)
            if len(st) > 1:
                c = st[-2] + st[-1]
                if c == "()":
                    st.pop()
                    st.pop()
        return len(st)
