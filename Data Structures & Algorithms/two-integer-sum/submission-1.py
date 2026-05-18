class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}

        for i, val in enumerate(nums):
            thisdict[val] = i
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in thisdict and thisdict[diff] != i:
                return [i, thisdict[diff]]
        