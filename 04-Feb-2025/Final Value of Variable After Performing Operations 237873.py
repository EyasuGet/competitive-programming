# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

x = 0
        for op in operations:
            if op[1] == "-":
                x -= 1
            else:
                x += 1
        return x