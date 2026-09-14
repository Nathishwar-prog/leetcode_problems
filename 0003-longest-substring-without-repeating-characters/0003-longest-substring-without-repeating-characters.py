class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Shrink the window until the character is unique
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])

            # Current window length
            max_length = max(max_length, right - left + 1)

        return max_length