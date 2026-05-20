class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = [None] * len(strs)

        for i in range(len(strs)):
            sortedStrs[i] = "".join(sorted(strs[i]))

        groups = {}

        for i in range(len(strs)):
            if sortedStrs[i] not in groups:
                groups[sortedStrs[i]] = []
            groups[sortedStrs[i]].append(strs[i])
        
        return list(groups.values())