class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set_nums = set(nums)
        # for i, num in enumerate(nums):
        #     if (target - num) in set_nums:
        #         j = nums.index(target-num)
        #         return [i,j]

        index_list = []
        for i,num in enumerate(nums):
            index_list.append([num,i])

        index_list.sort()
        i,j = 0, len(nums) - 1
        while i<j:
            cur = index_list[i][0] + index_list[j][0]
            if cur == target:
                return [min(index_list[i][1],index_list[j][1]),
                        max(index_list[i][1],index_list[j][1])]

            elif cur < target:
                i += 1
            
            else:
                j -= 1

        