from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt_area = int(area**0.5)
        for i in range(sqrt_area, 0, -1):
            if area % i == 0:
                return [area // i, i]