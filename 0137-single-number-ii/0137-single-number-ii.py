class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for i in range(32):
            bit_sum = 0

            for num in nums:
                bit_sum += (num >> i) & 1

            if bit_sum % 3 != 0:
                result |= (1 << i)

        # Convert to Python's signed 32-bit integer
        if result >= 2**31:
            result -= 2**32

        return result