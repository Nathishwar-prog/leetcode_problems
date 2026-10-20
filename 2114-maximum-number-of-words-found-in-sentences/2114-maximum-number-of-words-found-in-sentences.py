class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        largest = []
        for index in range(len(sentences)):
            largest.append(len(sentences[index].split(" ")))

        return max(largest)