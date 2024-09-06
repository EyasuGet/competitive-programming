class Solution(object):
    def lengthOfLastWord(self, s):
        se = []
        striped = s.strip()
        if len(striped) == 1:
            return 1
        if len(striped) == len(str(reversed(striped))):
            return len(striped)
        else:
            for i in reversed(striped):
                if i != " ":
                    se.append(i)
                else:
                    return len(se)
        return len(striped)