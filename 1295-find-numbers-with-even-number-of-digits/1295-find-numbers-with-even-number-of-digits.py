class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = 0
        # for num in nums:
        #     digit = 0
        #     while num > 0:
        #         digit  += 1
        #         num //= 10

        #     if digit % 2 == 0 :
        #         result += 1

        # return result 
        return sum(1 for num in nums if len(str(num)) % 2 == 0 )