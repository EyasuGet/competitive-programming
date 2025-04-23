# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/


    def simplifyPath(self, path: str) -> str:
        splitted = path.split("/")
        st = []
        for i in range(len(splitted)):
            if splitted[i] == "..":
                if st:
                    st.pop()
            elif splitted[i] == "." or splitted[i] == "":
                continue
            else:
                st.append(splitted[i])

        return "/" + "".join(st)