class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = []
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9' or 'A' <= char <= 'Z':
                alphanumeric.append(char.lower())

        n = len(alphanumeric)

        for i in range(n//2):
            iChar = alphanumeric[i]
            jChar = alphanumeric[len(alphanumeric)-i-1]
            if iChar != jChar:
                return False
        return True
