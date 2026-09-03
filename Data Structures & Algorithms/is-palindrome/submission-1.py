class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        l = 0
        r = len(new)-1
        while l < r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1

        return True

        