import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanStr = re.sub(r'[^0-9a-zA-Z]', '', s)
        reversedStr = cleanStr[::-1]
        return cleanStr.lower() == reversedStr.lower()