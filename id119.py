class Solution(object):
    def getRow(self, rowIndex):
        rs = [1]
        for i in range(1, rowIndex + 1):
            rs.append(1)
            for j in range(i - 1, 0, -1):
                rs[j] += rs[j - 1]
        return rs