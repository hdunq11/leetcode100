class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        
        rs = [[1]]
        
        for i in range(1, numRows):
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = rs[i-1][j-1] + rs[i-1][j]
                
            rs.append(row)
            
        return rs