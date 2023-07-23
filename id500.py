        
class Solution(object):
    """
        :type words: List[str]
        :rtype: List[str]
        """
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        valid_words = []
        for word in words:
            lowercase_word = word.lower()
            if set(lowercase_word).issubset(row1) or set(lowercase_word).issubset(row2) or set(lowercase_word).issubset(row3):
                valid_words.append(word)
        return valid_words