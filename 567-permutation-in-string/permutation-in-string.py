class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        n1 = len(s1)
        n2 = len(s2) 

        if n1 >  n2:
            return False
        #count of letter occurence
        s1_c = [0] * 26 
        s2_c = [0] * 26
        
        for i in range(n1):
            s1_c[(ord(s1[i])- 97)] += 1
            s2_c[ord(s2[i]) - 97] += 1
        if s1_c == s2_c:
            return True
        
        for i in range(n1,n2):
            s2_c[(ord(s2[i]) - 97)] += 1
            s2_c[ord(s2[i - n1]) - 97] -= 1

            if s1_c == s2_c:
                return True
        return False        