class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        
        mat1 = [num for row in mat for num in row]
        mat2 = [mat1[i*c:(i+1)*c] for i in range(r)]
        return mat2


        


  