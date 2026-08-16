class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        count = 0

        for x in nums:
            if x in freq:
                count += freq[x]

            freq[x] = freq.get(x,0) + 1

        return count