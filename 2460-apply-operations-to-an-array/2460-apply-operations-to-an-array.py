class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        write = 0 
        write2 = 0 

        for read in range(1,len(nums)):
            if nums[read] == nums[write]:
                nums[write] *= 2
                nums[read] = 0
            write+= 1

        for read in range(len(nums)):
            if nums[read] != 0 :
                nums[write2],nums[read] = nums[read],nums[write2]
                write2 += 1

        return nums

            