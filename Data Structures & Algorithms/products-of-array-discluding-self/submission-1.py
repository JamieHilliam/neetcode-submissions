class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_excl_zero = 1
        for curr in nums:
            if curr != 0:
                product_excl_zero *= curr
            else:
                zero_count+=1
        product_list=[]
        for i in range(len(nums)):
            if zero_count == 0:
                curr_product = product_excl_zero/nums[i]
            elif zero_count == 1:
                if nums[i] == 0:
                    curr_product = product_excl_zero
                else:
                    curr_product = 0
            else:
                curr_product = 0
            product_list.append(int(curr_product))
        return product_list