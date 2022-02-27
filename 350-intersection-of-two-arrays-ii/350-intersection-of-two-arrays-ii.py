class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, res = {},[]
        for num in nums1:
            dic[num]=dic[num]+1 if num in dic else 1
        for num2 in nums2:
            if num2 in dic and dic[num2]>0:
                res.append(num2)
                dic[num2] -= 1
        return res