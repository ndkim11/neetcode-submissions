class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zeros = 0
        for i, num in enumerate(nums):
            # if num is zero
            if not num:
                zeros += 1
                zero_ind = i

                # more than 1 zero
                if zeros > 1:
                    return [0]*len(nums)

            # not zero
            else:
                total_prod *= num

        ans = []

        if zeros:
            ans = [0]*len(nums)
            ans[zero_ind] = total_prod
            return ans

        for num in nums:
            ans.append(total_prod//num)

        return ans