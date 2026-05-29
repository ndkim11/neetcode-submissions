class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for low in range(n):
            if nums[low] > 0:
                break

            # low index is bigger than 0 (at least 1)
            if low > 0 and nums[low] == nums[low-1]:
                continue

            left, right = low+1, n-1
            while left<right:
                if nums[left] + nums[right] + nums[low] == 0:
                    ans.append([nums[low],nums[left],nums[right]])
                    left,right = left+1,right-1
                    # Make sure they are not the same numbers
                    while left<right and nums[left] == nums[left-1]:
                        left += 1

                    while left<right and nums[right]== nums[right+1]:
                        right -= 1
                
                elif nums[left]+nums[right] + nums[low] < 0:
                    left += 1

                else:
                    right -= 1

        return ans