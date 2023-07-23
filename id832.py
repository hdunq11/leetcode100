class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        return [[image[i][n-1-j] ^ 1 for j in range(n)] for i in range(n)]