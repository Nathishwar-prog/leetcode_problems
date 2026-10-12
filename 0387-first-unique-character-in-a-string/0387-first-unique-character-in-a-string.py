class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = {}

        for char in s :
            seen[char] = seen.get(char,0) + 1

        for i , val in enumerate(s):
            if seen[val] == 1:
                return i 

        return -1
        