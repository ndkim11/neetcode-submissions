class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        ins_loc = len(nums)

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                ins_loc = mid
                r = mid -1

            else:
                l = mid + 1

        # target is smaller than 0th element
        return ins_loc

            