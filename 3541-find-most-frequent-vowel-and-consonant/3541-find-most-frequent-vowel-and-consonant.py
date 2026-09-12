class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        vowels = [
            freq
            for char, freq in count.items()
            if char in "aeiou"
        ]

        consonants = [
            freq
            for char, freq in count.items()
            if char not in "aeiou"
        ]

        max_vowel = max(vowels) if vowels else 0
        max_consonant = max(consonants) if consonants else 0

        return max_vowel + max_consonant


        
        