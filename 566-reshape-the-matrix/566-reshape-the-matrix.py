class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        if n*m!=r*c:
            return mat
        
        arr=[]
        for row in mat:
            for num in row:
                arr.append(num)
        res = [[0 for i in range(c)] for j in range(r)]
        k=0
        for i in range(r):
            for j in range(c):
                res[i][j]=arr[k]
                k+=1
        
        return res