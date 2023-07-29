class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        odd_count = 0
        for count in char_count.values():
            if count % 2 == 1:
                odd_count += 1
        if odd_count <= 1:
            return len(s)
        else:
            return len(s) - odd_count + 1