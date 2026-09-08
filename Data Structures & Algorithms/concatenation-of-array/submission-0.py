class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output_list = []
        for i in range(len(nums)*2):
            i = i % len(nums)
            output_list.append(nums[i])
        return output_list
