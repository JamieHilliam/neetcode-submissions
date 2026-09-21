class Solution:
    def twoSum(self, start_index, sorted_nums, target):
        l, r = start_index, len(sorted_nums) - 1
        results = []
        while l < r:
            current_left = sorted_nums[l]
            current_right = sorted_nums[r]
            current_sum = current_left + current_right
            if current_sum == target:
                current_result = [current_left, current_right]
                results.append(current_result)
                while l < r and sorted_nums[l] == current_left:
                    l += 1
                while l < r and sorted_nums[r] == current_right:
                    r -= 1
                continue

            if current_sum < target:
                l += 1
                continue
            if current_sum > target:
                r -= 1
                continue
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        results = []
        for index, num in enumerate(sorted_nums):
            if index > 0 and num == sorted_nums[index - 1]:
                continue
            current_results = self.twoSum(index + 1, sorted_nums, -num)
            if current_results:
                for curr in current_results:
                    tup = []
                    tup.append(num)
                    tup.append(curr[0])
                    tup.append(curr[1])
                    results.append(tup)
                
        return results