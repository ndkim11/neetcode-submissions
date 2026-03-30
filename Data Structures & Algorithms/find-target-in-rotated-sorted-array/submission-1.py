class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        # l and r meet --> Min value
        while l < r:
            mid = (l+r)//2
            # smallest belongs right of mid
            if nums[mid] > nums[r]:
                l = mid + 1
            # smallest belongs left or same as mid
            else:
                r = mid

        min_idx = l

        def bin_search(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = mid+1

                else:
                    right= mid-1

            return -1

        result = bin_search(0,min_idx -1)
        if result != -1:
            return result
        
        return bin_search(min_idx, len(nums)-1)
