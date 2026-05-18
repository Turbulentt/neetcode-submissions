class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in thisdict:
                return [thisdict[diff], i]
            thisdict[val] = i