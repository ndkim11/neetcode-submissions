class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_ele = nums[left] 

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < min_ele:
                min_ele = nums[mid]
                right = mid -1

            else:
                left = mid + 1

        return min_ele