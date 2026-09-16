class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        num_list = sorted(list(num_set))
        lengths = []
        counter = 1
        for i in range(1, len(num_list)):
            cur_val = num_list[i]
            if num_list[i-1] != cur_val - 1:
                counter = 1
            else:
                counter += 1
            lengths.append(counter)

        if not lengths:
            return 1 if num_list else 0
        return max(lengths)

# 2,3,4,4,5,10,20
