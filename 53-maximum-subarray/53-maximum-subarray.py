class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum,run_sum=-212121313133,0
        for num in nums:
            run_sum+=num
            max_sum=max(max_sum,run_sum)
            run_sum=max(0,run_sum)
            
        return max_sum