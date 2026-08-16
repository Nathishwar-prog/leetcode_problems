class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1

        sorted_arr = sorted(freq,key=freq.get,reverse=True)

        return sorted_arr[:k]

        for num in freq:
            if freq[num] > 1 and len(most_frequent) <= k:
                most_frequent.append(num)

        