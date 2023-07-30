class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y  
        rs = 0

        while xor != 0:
            if xor & 1:
                rs += 1
            xor >>= 1 

        return rs