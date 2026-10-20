class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False 