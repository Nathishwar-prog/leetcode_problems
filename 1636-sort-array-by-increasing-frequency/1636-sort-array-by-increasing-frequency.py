class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        '''
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        nums.sort(key=lambda num: (freq[num], -num))

        return nums
        '''
        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Lowest frequency first
        for count in range(1, len(buckets)):
            # Same frequency -> larger value first
            for num in sorted(buckets[count], reverse=True):
                result.extend([num] * count)

        return result