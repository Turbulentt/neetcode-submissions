class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(x.lower() for x in s if x.isalnum())

        left, right = 0, len(newS) - 1
        while left <= right:
            if newS[left].lower() != newS[right].lower():
                return False
            left += 1
            right -= 1

        return True