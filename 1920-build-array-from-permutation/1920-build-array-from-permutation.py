class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []

        for i in range(len(nums)):
            arr.append(nums[nums[i]])

        return arr

            
