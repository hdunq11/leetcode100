class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)