class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(x.lower() for x in s if x.isalnum())

        return newS == newS[::-1]