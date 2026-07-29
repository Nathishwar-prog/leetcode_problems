class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            digit = x % 10
            # Overflow condition
            if reverse > 214748364 or (reverse == 214748364 and digit > 7):
                return 0
            
            reverse = reverse * 10 + digit
            x = x // 10

        return (sign * reverse)