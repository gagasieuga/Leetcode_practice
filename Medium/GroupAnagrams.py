from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        newStr = defaultdict(list) 
        for str in strs:
            sorted_str = tuple(sorted(str))
            newStr[sorted_str].append(str)        
        return newStr.values()