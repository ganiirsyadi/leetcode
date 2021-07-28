from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False

solution = Solution()
print(solution.containsDuplicate([2,14,18,22,22]))

"""
Runtime: 126 ms, faster than 31.01% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.8 MB, less than 87.52% of Python3 online submissions for Contains Duplicate.
"""