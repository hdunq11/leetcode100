class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        count = 0
        for j in range(m):
            for i in range(1, n):
                if strs[i][j] < strs[i-1][j]:
                    count += 1
                    break
        return count