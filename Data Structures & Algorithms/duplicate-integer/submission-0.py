class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        for x in nums:
            newSet.add(x)
        
        return len(newSet) != len(nums)