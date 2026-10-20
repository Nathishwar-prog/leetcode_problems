class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highest = max(candies)
        op = []
        for val in candies:
            if val + extraCandies >= highest:
                op.append(True)
            else:
                op.append(False)

        return op 