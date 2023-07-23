class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = n & 1
        while n > 0:
            n >>= 1
            c1 = n & 1
            if c1 == bit:
                return False
            bit = c1
        return True