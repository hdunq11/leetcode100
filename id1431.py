class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies) 

        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res # trả về danh sách kết quả


candies_str = input()
candies = [int(c) for c in candies_str.split()]

# Nhập số kẹo bổ sung từ bàn phím
extra_candies = int(input())

# Tạo đối tượng Solution và gọi phương thức kidsWithCandies
s = Solution()
result = s.kidsWithCandies(candies, extra_candies)

# In kết quả ra màn hình
print("Kết quả: ", result)