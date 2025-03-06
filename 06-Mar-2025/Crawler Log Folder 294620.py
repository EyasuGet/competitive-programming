# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        
        for i in logs:
            if i == "../":
                if st:
                    st.pop()
            elif i == "./":
                continue
            else:
                st.append(1)
        return len(st)
