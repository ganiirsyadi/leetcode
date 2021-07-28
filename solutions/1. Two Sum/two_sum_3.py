from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		value_index_dict = {}
		
		for i,n in enumerate(nums):
			if n in value_index_dict:
				value_index_dict[n].append(i)
			else:
				value_index_dict[n] = [i]
		for value in value_index_dict.keys():
			try:
				diff = target - value
				if value == diff:
					return [value_index_dict[value][0], value_index_dict[value][1]]
				return [value_index_dict[value][0], value_index_dict[target - value][0]]
			except:
				pass

	def main(self):
		print(self.twoSum([2,7,11,15], 9))
		print(self.twoSum([3,2,4], 6))
		print(self.twoSum([3,3], 6))
    
s = Solution()
s.main()

"""
Runtime: 68 ms, faster than 53.29% of Python3 online submissions for Two Sum.
Memory Usage: 16.3 MB, less than 9.18% of Python3 online submissions for Two Sum.
"""