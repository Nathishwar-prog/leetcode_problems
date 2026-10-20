class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        value = 0
        for op in operations:
            if op == "--X" or op == "X--":
                value -= 1
            elif op == "++X" or op == "X++":
                value += 1

        return value