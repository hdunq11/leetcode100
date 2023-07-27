class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        
        count = 0
        for n in range(left, right+1):
            bits = bin(n).count('1')
            if is_prime(bits):
                count += 1
        return count