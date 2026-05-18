class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            k = thisdict.get(diff)
            if k is not None:
                return [k, i]

            thisdict[nums[i]] = i