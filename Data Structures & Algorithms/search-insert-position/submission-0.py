class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            
            # Target found
            if nums[mid] == target:
                print('target found')
                return mid

            # Target is smaller
            elif nums[mid] > target:
                right = mid -1

            else:
                left = mid + 1
        
        return left