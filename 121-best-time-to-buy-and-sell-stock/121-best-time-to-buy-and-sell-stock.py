class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min=prices[0]
        res=0
        for num in prices:
            res=max(res,num-left_min)
            left_min=min(left_min,num)
        
        return res