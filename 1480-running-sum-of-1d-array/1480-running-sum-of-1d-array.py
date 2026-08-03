class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixArr = [0]* len(nums)
        prefixArr[0] = nums[0]

        for i in range(1,len(nums)):
            prefixArr[i] = nums[i] + prefixArr[i - 1]

        return prefixArr