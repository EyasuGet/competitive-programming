from typing import Counter

from pyparsing import C

def kth_unique():
    k=2
    arr = ["d","b","c","b","c","a"]
    unique=[]
    answer = ""
    map = dict(Counter(arr))
    for key,value in map.items():
        if value == 1:
            unique.append(key)
    print(unique)
    if k > len(unique):
        return answer
    else:
        return unique[k-1]
print(kth_unique())