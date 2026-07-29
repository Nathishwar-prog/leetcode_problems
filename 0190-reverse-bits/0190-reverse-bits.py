class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        reverse=0
        for _ in range(32):
            bit = n & 1
            reverse <<= 1
            reverse |= bit 
            n >>=1

        return reverse