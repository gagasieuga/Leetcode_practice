class Solution(object):
    def romanToInt(self, s):
        symbolMap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        totalSum = 0
        totalSum += symbolMap[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            totalSum += symbolMap[s[i]]
            if symbolMap[s[i]] < symbolMap[s[i+1]]:
                totalSum -= 2*symbolMap[s[i]]
        return totalSum