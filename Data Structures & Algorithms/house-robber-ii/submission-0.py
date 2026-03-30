class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.partial_rob(nums[1:]), self.partial_rob(nums[:-1]), nums[0])

    def partial_rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0, 0
        # rob1, rob2, current
        for n in nums:
            temp = max(rob_2, rob_1 + n)
            rob_1 = rob_2
            rob_2 = temp
        return rob_2
