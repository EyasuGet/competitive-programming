# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        file_name = {}
        for element in paths:
            arr = element.split()

            for name in arr[1:]:
                filename, content = name.split('(')
                path = arr[0] + '/' + filename
                if content in file_name:
                    file_name[content].append(path)
                else:
                    file_name[content] = [path]
        
        result = []
        
        
        for key, val in file_name.items():
            if len(val) > 1:
                result.append(file_name[key] )
        return result
