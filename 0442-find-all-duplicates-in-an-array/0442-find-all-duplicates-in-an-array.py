class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []

        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1

        return [x for x in freq if freq[x] > 1]