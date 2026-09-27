class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        positive_count = 0
        negative_count = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[i] < 0 :
                    negative_count += 1
                    continue

                positive_count += 1

        return max(positive_count , negative_count)

                