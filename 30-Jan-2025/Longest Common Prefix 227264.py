# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return word[:i]
        return strs[0]