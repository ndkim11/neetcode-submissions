class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def subSum(start, remain, current_comb):
            if remain == 0:
                ans.append(list(current_comb))
                return
            if remain < 0:
                return

            # start index --> duplicate x
            for i in range(start, len(nums)):
                num = nums[i]
                current_comb.append(num)

                # 같은 원소를 여러 번 쓸 수 있으므로 start 위치로 i를 전달
                subSum(i, remain - num, current_comb)

                # backtracking (back to original)
                current_comb.pop()
        
        subSum(0, target, [])
        return ans