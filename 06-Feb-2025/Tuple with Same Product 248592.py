# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

product_frq = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = nums[i]*nums[j]
                product_frq[prod] = product_frq.get(prod, 0 ) + 1

        combination = 0
        for value in product_frq.values():
            if value > 1:
                n = value - 1
                #finding the summation of n -1 and product with 8
                sum_of_n = 0
                while n > 0:
                    sum_of_n += n
                    n -= 1
                combination += ((sum_of_n) * 8)
        return combination