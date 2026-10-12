class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                current = num
                length = 1

                while current + 1 in nums:
                    current += 1
                    length += 1

                longest = max(length , longest)

        return longest

            