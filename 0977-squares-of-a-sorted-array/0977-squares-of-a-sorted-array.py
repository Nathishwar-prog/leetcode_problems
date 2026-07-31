class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left = 0
        right = n-1
        write = n-1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[left] * nums[left]
                left +=1
            else:
                result[write] = nums[right] * nums[right]
                right -=1

            write -=1
        return result
        