# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        chars = {'+', '-', '(', ')', ' '}
        ##check if its an email
        ans = []
        if "@" in s:
            adress, domain = s.split("@")

            ans.append(adress[0].lower() + "*****" + adress[-1].lower() + "@")

            for i in domain:
                ans.append(i.lower())
            return "".join(ans)
        
        else:
            ans = []
            for i in s:
                if i not in chars:
                    ans.append(i)
            # the last 4 characters
            local_num = "".join(ans[-4::])

            if len(ans) == 10:
                return "***-***-" + local_num
            elif len(ans) == 11:
                return "+*-***-***-" + local_num
            elif len(ans) == 12:
                return "+**-***-***-" + local_num
            else:
                return "+***-***-***-" + local_num
            




