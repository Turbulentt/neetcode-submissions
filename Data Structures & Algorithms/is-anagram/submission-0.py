class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = ''.join(sorted(s))
        t2 = ''.join(sorted(t))
        return t2 == s2