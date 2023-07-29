class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = {}
        for char in s:
            if char in c:
                c[char] += 1
            else:
                c[char] = 1
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1