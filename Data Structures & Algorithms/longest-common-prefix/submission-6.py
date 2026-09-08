class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix=""
        first_item = strs[0]

        for i in range(len(first_item)+1):
            curr_prefix = first_item[:i]
            prefix_in_all = True
            for curr_item in strs:
                if  not curr_item.startswith(curr_prefix):
                    prefix_in_all = False
            if prefix_in_all:
                longest_prefix = curr_prefix;
        return longest_prefix
                