from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]
        return False

solution = Solution()
print(solution.containsDuplicate([2,14,18,22,22]))

"""
Runtime: 128 ms, faster than 30.99% of Python3 online submissions for Contains Duplicate.
Memory Usage: 18.6 MB, less than 99.08% of Python3 online submissions for Contains Duplicate.
"""