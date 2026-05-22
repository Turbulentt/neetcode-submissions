class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        result = [None] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        result[0] = suffix[1]
        result[len(nums)-1] = prefix[len(nums)-2]
        for i in range(1, len(nums)-1):
            result[i] = prefix[i-1] * suffix[i+1]

        return result