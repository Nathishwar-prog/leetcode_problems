class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i+=1

            else:
                result.append(nums2[j])
                j+=1

        result.extend(nums1[i:m])
        result.extend(nums2[j:n])

        nums1[:m+n] = result # Remember this logic