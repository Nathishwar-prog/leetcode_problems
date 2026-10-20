class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newAddress = address.split(".")
        return "[.]".join(newAddress)