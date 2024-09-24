class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        c = 0
        for i in str(num):
            if num % int(i) == 0:
                c += 1
        return c
        # t,u=0,num
        # while u>0:
        #     k=u%10
        #     if num%k==0 and k!=0:
        #         t+=1
        #     u=u//10
        # return t