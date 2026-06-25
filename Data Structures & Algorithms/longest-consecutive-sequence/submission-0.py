class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) - no sorting
        # 2 20 4 10 3 (234)
        # heap? dict?
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num-1) not in num_set:
                cur_num = num
                cur_count = 1

                while (cur_num+1) in num_set:
                    cur_num += 1
                    cur_count += 1

                longest = max(longest, cur_count)

        return longest