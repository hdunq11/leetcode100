class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars = {}
        
        for char in magazine:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        
        for char in ransomNote:
            if char in chars and chars[char] > 0:
                chars[char] -= 1
            else:
                return False
        
        return True