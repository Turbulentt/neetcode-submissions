class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped = defaultdict(list)

        for n in nums:
            mapped[n].append(n)

        return sorted(mapped, key=lambda k: len(mapped[k]), reverse=True)[:k]