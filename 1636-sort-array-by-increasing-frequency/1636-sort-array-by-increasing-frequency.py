class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        nums.sort(key=lambda x : (freq[x] , -x)) # this is pilot condition

        return nums