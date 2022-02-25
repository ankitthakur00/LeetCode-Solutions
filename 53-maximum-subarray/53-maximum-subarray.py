class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run_sum,max_sum=0,-123454364645654
        for num in nums:
            run_sum+=num
            max_sum=max(max_sum,run_sum)
            run_sum=max(run_sum,0)
        return max_sum
        