class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set1, set2 = set(list1), set(list2)
        common_strings = set1 & set2
        min_sum = float('inf')
        rs = []
        for s in common_strings:
            i = list1.index(s)
            j = list2.index(s)
            if i + j < min_sum:
                min_sum = i + j
                rs = [s]
            elif i + j == min_sum:
                rs.append(s)
        return rs