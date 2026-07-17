from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            combies = combinations(nums,i)
            for combi in combies:
                ans.append(list(combi))

        return ans