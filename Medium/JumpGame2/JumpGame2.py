class Solution(object):
    def jump(self, nums):
        l = r = 0
        res = 0
        while (r < len(nums) - 1):
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest 
            res += 1
        return res
         