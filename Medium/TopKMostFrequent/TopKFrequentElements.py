from  collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countMap = defaultdict(int)
        result = []
        for i in nums:
            countMap[i] += 1
        freqCount = sorted(countMap.values(), reverse = True)
        #always add the first element
        result += (list(filter(lambda x: countMap[x] == freqCount[0], countMap))) 
        for i in range(1, k):
            # avoid duplicate elements
            if freqCount[i] != freqCount[i-1]:
                result += (list(filter(lambda x: countMap[x] == freqCount[i], countMap))) 
        return result