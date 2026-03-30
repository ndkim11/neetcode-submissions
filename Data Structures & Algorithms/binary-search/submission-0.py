class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        nums = [-1,0,2,4,6,8], target = 3
        (0,7) -> (0,3) -> (1,3) -> (2,3) -> (2,2) != 3
        '''
    
        nlens = len(nums)
        end = nlens - 1
        start = 0

        while start <= end:
            mid = int((start+end)/2)
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                end = mid-1

            else:
                start = mid+1

        return -1
        