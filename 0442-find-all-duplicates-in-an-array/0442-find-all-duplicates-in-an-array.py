class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for x in nums:
            index = abs(x) - 1

            if nums[index] < 0:
                result.append(abs(x))
            else:
                nums[index] = -nums[index]

        return result