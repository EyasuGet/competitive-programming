from collections import Counter
def canConstruct(ransomNote, magazine):
    a = Counter(ransomNote)
    b = Counter(magazine)

    for i in a.keys():
        print(a[i],b[i])
        if i not in b.keys():
            return False
        elif a[i] <= b[i]:

            return True
    return False