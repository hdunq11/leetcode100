class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left] if left < len(letters) else letters[0]