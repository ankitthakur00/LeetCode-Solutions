class Solution(object):
    def climbStairs(self, n):
        
        cs=[]
        cs.append(1)
        cs.append(2)
        for i in range(2,n):
            cs.append(cs[i-1]+cs[i-2])
            
        return cs[n-1]