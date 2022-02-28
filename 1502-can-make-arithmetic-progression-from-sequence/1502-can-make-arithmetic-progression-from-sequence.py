class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d=abs(arr[0]-arr[1])
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])!=d:
                return False
            
        return True