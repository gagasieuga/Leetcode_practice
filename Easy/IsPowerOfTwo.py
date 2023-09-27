class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n-1) == 0)
        ## if n and bit with n-1 = 0, then n should be a power of 2 due to bit logic