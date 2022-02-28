class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        prod=1
        while n:
            sum+=n%10
            prod*=n%10
            n//=10
        return prod-sum
        