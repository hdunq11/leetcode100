class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        e = []
        for char in s:
            if char.isalpha():
                e.append(char)

        e.reverse()
        result = []
        for char in s:
            if char.isalpha():
                result.append(e.pop(0))
            else:
                result.append(char)

        return "".join(result)