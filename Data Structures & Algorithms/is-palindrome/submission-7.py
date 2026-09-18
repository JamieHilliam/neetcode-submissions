class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) -1
        while l < r:
            # Non Alphanumeric case (skip)
            while l < r and not s[l].isalnum():
                l+= 1
            while l < r and not s[r].isalnum():
                r-=1
            # Not matching case (fail)
            if s[l].lower() != s[r].lower():
                return False
            # matching case (continue)
            l += 1
            r -= 1
        return True