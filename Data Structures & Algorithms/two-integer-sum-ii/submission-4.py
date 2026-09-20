class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind_1, ind_2 = 0, len(numbers) -1
        while ind_1 < ind_2:
            sum = numbers[ind_1] + numbers[ind_2] 
            if (sum == target):
                return [ind_1 + 1, ind_2 + 1]
            elif (sum < target):
                ind_1 += 1
            else:
                ind_2 -= 1
        return []