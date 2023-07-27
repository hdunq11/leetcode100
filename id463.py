class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rs = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rs += 4
                    if i > 0 and grid[i-1][j] == 1: 
                        rs -= 2
                    if j > 0 and grid[i][j-1] == 1: 
                        rs -= 2
                        
        return rs