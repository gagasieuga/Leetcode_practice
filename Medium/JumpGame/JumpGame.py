class Solution(object):
    def canJump(self, nums):
        reachable = 0
        for i, jump_power in enumerate(nums):
            if (reachable < i):
                return False
            reachable = max(reachable, jump_power + i)
        return True
            
        