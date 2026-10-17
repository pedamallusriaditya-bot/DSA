class Solution(object):
    def maxProductPair(self, nums, target):
        max_product=float("-inf")
        best_pair=[-1, -1]
        seen={}
        for j, num in enumerate(nums):
            complement=target-num
            if complement!=num and complement in seen:
                product=num*complement
                if product > max_product:
                    max_product=product
                    i=seen[complement]
                    best_pair=[j, i] if num > complement else [i, j]
            if num not in seen:
                seen[num]=j
        return best_pair
        