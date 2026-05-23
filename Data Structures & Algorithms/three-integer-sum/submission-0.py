class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        myDict = {}

        for i in range(len(nums)-1, -1, -1):
            if nums[i] in myDict:
                continue
            else:
                myDict[nums[i]] = i
        
        for i in range(len(nums)-2):
            for k in range(i+1, len(nums)-1):
                diff = -(nums[i] + nums[k])

                if diff in myDict and myDict[diff] > k:
                    triplet = sorted([nums[i], nums[k], diff])

                    if tuple(triplet) not in seen:
                        seen.add(tuple(triplet))
                        result.append(triplet)

        return result
