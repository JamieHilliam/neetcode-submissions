class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()

        for curr_num in nums:
            if curr_num in seen_set:
                return True
            seen_set.add(curr_num)
        return False

        