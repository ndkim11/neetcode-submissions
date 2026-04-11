class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_nums = {}
        for i,num in enumerate(nums):
            dic_nums[num] = i
        
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dic_nums and dic_nums[diff] != i:
                # return [min(i,dic_nums[diff]), max(i,dic_nums[diff])]
                return [i,dic_nums[diff]]

        return []