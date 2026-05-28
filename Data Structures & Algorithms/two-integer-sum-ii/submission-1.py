class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers)-1
        while left < right:
            l_num, r_num = numbers[left], numbers[right]
            # Target pair found
            if l_num + r_num == target:
                return [left+1,right+1]

            # Target smaller than sum
            elif l_num+r_num > target:
                right -=1

            # Target bigger than sum
            elif l_num+r_num < target:
                left +=1
            