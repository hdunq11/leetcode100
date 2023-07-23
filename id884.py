class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        word_dict = {}
        for word in s1.split():
            word_dict[word] = word_dict.get(word, 0) + 1
        for word in s2.split():
            word_dict[word] = word_dict.get(word, 0) + 1
        uncommon = [word for word, count in word_dict.items() if count == 1 and (word in s1 or word in s2)]
        
        return uncommon