class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums1)
        m=len(nums2)
        ketqua=[]
        for i in range(n):
            for j in range(m):
                if nums1[i]==nums2[j] :
                    k = j + 1
                    while k < m and nums2[k] <= nums1[i]:
                        k += 1
                    if k < m and nums2[k] > nums1[i]:
                        ketqua.append(nums2[k])
                    else:
                        ketqua.append(-1)
        return ketqua