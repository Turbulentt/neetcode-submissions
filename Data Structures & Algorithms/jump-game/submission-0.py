class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpRem = 0

        for i in range(len(nums)-1):
            jumpRem = max(jumpRem, nums[i])
            jumpRem -= 1
            if jumpRem < 0:
                return False
        
        return True