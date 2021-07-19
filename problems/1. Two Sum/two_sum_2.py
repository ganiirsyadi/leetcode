from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		value_index_dict = {} # value : index

		# enumerates return index, value pair of a list
		for index, element in enumerate(nums):
			diff = target - element
			if diff in value_index_dict:
				return [value_index_dict[diff], index]
			value_index_dict[element] = index
	
	def main(self):
		print(self.twoSum([2,7,11,15], 9))
		print(self.twoSum([3,2,4], 6))
		print(self.twoSum([3,3], 6))
    
s = Solution()
s.main()

"""
Runtime: 60 ms, faster than 76.68% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 40.97% of Python3 online submissions for Two Sum.
"""