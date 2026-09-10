class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        min_len = min(len(word1), len(word2))
        for curr_index in range(min_len):
            merged_string.append(word1[curr_index])
            merged_string.append(word2[curr_index])
        if len(word1) > min_len:
            longer_word = word1
        else:
            longer_word = word2
        
        if len(longer_word) > min_len:
            for i in range(min_len, len(longer_word)):
                merged_string.append(longer_word[i])
        return ''.join(merged_string)
        