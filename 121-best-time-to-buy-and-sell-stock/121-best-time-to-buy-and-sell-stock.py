class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min,res = prices[0],0
        for num in prices:
            res=max(res,num-left_min)
            left_min=min(left_min,num)  
        return res