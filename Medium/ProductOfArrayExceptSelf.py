class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)
        result = [0] * (len(nums))
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i] #iterate prefix from 1 -> len(nums) 
            # first value is already 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = postfix[i+1] * nums[i] #iterate postfix from len(nums) - 1 -> 0
            # last value is already 1
        for i in range(len(nums)):
            result[i] = postfix[i+1] * prefix[i]
        return result