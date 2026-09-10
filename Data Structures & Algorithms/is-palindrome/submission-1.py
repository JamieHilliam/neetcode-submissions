class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Alphanum Stuff
        alphanum_list = []
        for current_char in s:
            if current_char.isalnum():
                alphanum_list.append(current_char)
        s = ' '.join(alphanum_list)
        split_list = s.split()
        joined_str = ''.join(split_list)
        joined_str = joined_str.lower()
        joined_len = len(joined_str)
        print(joined_str)
        for i in range(joined_len):
            if joined_str[i] != joined_str[joined_len - i -1]:
                return False
        return True
