class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_numbers = sorted(set(nums))
        nums[:len(unique_numbers)] = unique_numbers
        return len(unique_numbers)