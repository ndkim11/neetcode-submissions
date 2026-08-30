class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combies = []
        arr = []
        N = len(nums)

        def tree(i):
            if i == N:
                combies.append(arr.copy())
                return

            arr.append(nums[i])
            tree(i+1)
            arr.pop()
            tree(i+1)

        tree(0)
        return combies