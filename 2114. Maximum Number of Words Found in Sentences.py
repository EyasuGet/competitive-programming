class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        r = 0
        for s in sentences:
            s = s.split() #turns them into a list of wordsv["alice","bob"]
            l = len(s)
            r = max(r, l)
    
        return r

        # count = 0
        # for i in sentences:
        #     length = len(re.findall(" ",i)) + 1  #re.findall(pattern, text)
    
        #     count = max(length,count)
        
        # return count
        