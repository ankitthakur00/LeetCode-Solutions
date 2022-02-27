class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        i=0
        for num in nums:
            d[num]=i
            i+=1
        i=0
        for num in nums:
            if target-num in d.keys() and i!=d[target-num]:
                return [i,d[target-num]]
            i+=1
        return []
        