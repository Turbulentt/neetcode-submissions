class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        nums.sort()

        curr = -100
        streak = 1
        for x in nums:
            if x == curr+1:
                streak += 1
                curr = x
            if x > curr+1:
                if result < streak:
                    result = streak
                streak = 1
                curr = x
        
        return max(result, streak)