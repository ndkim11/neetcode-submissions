class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        m_sum = [0] * nums_len # empty list of maximum sum until ith house
        for i in range(nums_len):
            if i == 0:
                m_sum[0] = nums[0]
            elif i == 1:
                m_sum[i] = max(m_sum[i-1], nums[i])
            else:
                m_sum[i] = max(m_sum[i-1], m_sum[i-2] + nums[i])

        return m_sum[nums_len-1]
        