from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        
        dictionary = dict(Counter(arr))
        dupilicate = []
        for value in dictionary.values():
            dupilicate.append(value)
        return len(set(dupilicate)) == len(dupilicate)

        #              others code that i liked
        # count={}
        # unique=set()

        # for num in arr:
        #     if num not in count:
        #         count[num]=1
        #     else:
        #         count[num]+=1

        # for c in count.values():
        #     if c in unique:
        #         return False
        #     else:
        #         unique.add(c)
        # return True