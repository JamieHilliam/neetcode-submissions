class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_copy = s.copy()
        s_length = len(s)
        for i in range(s_length):
            s[i] = s_copy[s_length - i -1]
        

        